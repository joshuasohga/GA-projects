import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
# import libraries
import pickle
import seaborn as sns
import scipy.stats as stats
import warnings
warnings.filterwarnings('ignore')
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, train_test_split, KFold
from sklearn.linear_model import LinearRegression, Lasso, LassoCV, Ridge, RidgeCV, ElasticNet, ElasticNetCV 
from sklearn.metrics import mean_squared_error
from sklearn.dummy import DummyRegressor
from pathlib import Path

enet = ElasticNet
sns.set_style()

pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:.2f}'.format #suppress scientific notations when using the Describe function
pd.options.display.float_format = "{:,.2f}".format
train_csv = Path(__file__).parents[1] / 'wrex303/Capstone/train.csv'
train = pd.read_csv(train_csv)

train = train.iloc[:, 1:] #remove unnamed columns
train_dummies = pd.get_dummies(train, drop_first = True) #onehotencoding the team_names

x = train_dummies.loc[:, train_dummies.columns != 'xpm']
y = train_dummies[['xpm']]

print(x.shape)
print(y.shape)

# train test split
xtest, xtrain, ytest, ytrain = train_test_split(x, y, test_size = 0.3, random_state = 42)
    
print(xtrain.shape)
print(ytrain.shape)

# scale data - standardscaler
scaler = StandardScaler()

xtrain_scaled = scaler.fit_transform(xtrain)
xtest_scaled = scaler.transform(xtest)

pickle.dump(scaler, open('./scaler.bin', 'wb')) #save it in a pickle for prediction based on input later


enet_alpha = np.arange(0, 1, 0.005)
enet_ratio = [.01, .1, .2, .3, .5, .7, .9, .95, .99, 1]

# define CV function
nfolds = 5 
np.random.seed(100)

def crossval(model, x, y):
    kf = KFold(nfolds, shuffle = True, random_state = 7)
    rmse = np.sqrt(-cross_val_score(model, x, y, cv = kf, scoring = 'neg_mean_squared_error'))
    r2 = cross_val_score(model, x, y, cv = kf)
    return 'mean CV R2:', r2.mean(), \
            'mean CV RMSE:', rmse.mean(), \
            'CV R2 variance:', r2.var(), \
            'CV RMSE variance:', rmse.var()



# fits multiple alphas and rhos
enetcv = ElasticNetCV(alphas = enet_alpha, l1_ratio = enet_ratio, cv = 5)
enetcv = enetcv.fit(xtrain_scaled, ytrain)
enet = ElasticNet(alpha = enetcv.alpha_, l1_ratio = enetcv.l1_ratio_)
print('optimal enet alpha: ', enetcv.alpha_)
print('optimal enet lambda: ', enetcv.l1_ratio_)
print('best elastic net R2: ', enetcv.score(xtrain_scaled, ytrain))
enet_mod = enet.fit(xtrain_scaled, ytrain)


def predict_xpm(team_name):    
    for each_key, _ in train_dummies.items():
        if team_name in each_key:
            team_name_df = train_dummies[train_dummies[f'name_{team_name}'] == 1]
            custom_test_df = pd.DataFrame(data = dict(zip(train_dummies.keys(), team_name_df.mean())), index = [0])
            x_custom = custom_test_df.loc[:, custom_test_df.columns != 'xpm']
            y_custom = custom_test_df[['xpm']]
            scaler = pickle.load(open('./scaler.bin', 'rb'))
            x_custom_scaled = scaler.transform(x_custom)
            ypred = enet_mod.predict(x_custom_scaled)
            a =int(ypred[0])
            b = int(y_custom.xpm[0])
            
            plk = f"The model predicts {team_name}'s XPM to be {a}. Actual XPM is {b}." 
            return plk
        
        
predict_xpm("Team Liquid")         
abc = {'PSG.LGD','Team Spirit'}
option = st.selectbox(
     'Which team would you like to predict?',
     (abc))
uhno = predict_xpm(option)
st.write('You selected:', option, uhno)
