all_hyper_parameter_dic={'randomforestclassifier':{
          'n_estimators':range(20,200,20),
          'criterion':['gini', 'entropy'],
          'min_samples_split':range(2,5),
          'min_samples_leaf':range(1,4),
          'ccp_alpha':[0.1,0.2,0.001,0.002,0.02]
      },

'logisticregression':{
         'C':[1.0,2.0,0.2,0.3,0.5,0.9,0.8,2.1,2.5],
          'max_iter':range(100,300,50),
          'random_state':[1,10,100,20,82,727,11,525,62,98,524]
          },



'svc':{
          'C':[1.0,2.0,0.2,0.3,0.5,0.9,0.8,3.0],
          'kernel':['linear', 'poly', 'rbf', 'sigmoid'],
          'gamma':['scale', 'auto'],
          
          'max_iter':range(100,300,50),
          'random_state':range(1,20,2)},

'xgbclassifier':{
          'booster':['gbtree', 'gblinear']},


'decisiontreeclassifier':{
            'criterion':['gini','entropy'],
          'splitter':['best', 'random'],
          'min_samples_split':range(2,5),
          
          'min_samples_leaf':range(1,4),
          'ccp_alpha':[0.1,0.2,0.001,0.002,0.02]},

'kneighborsclassifier':{
    'n_neighbors':range(1,10,2),
    'weights':['uniform', 'distance']},

'naive_bayes_Gaus':{},


'linearregression':{},

'kneighborsregressor':{'n_neighbors':range(1,10,2),'weights':['uniform','distance'],
         'algorithm':['auto', 'ball_tree', 'kd_tree', 'brute']}

,'randomforestregressor':{
          'n_estimators':range(10,200,20),
          'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
          'min_samples_split':range(2,5),
          'min_samples_leaf':range(1,4),
          'ccp_alpha':[0.1,0.2,0.001,0.002,0.02]
      },

'decisiontreeregressor':{

          'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
          'splitter':['best', 'random'],
          'min_samples_split':range(2,5),
    
          'min_samples_leaf':range(1,4),
          'ccp_alpha':[0.1,0.2,0.001,0.002,0.02]},
'xgbregressor':{
          'booster':['gbtree', 'gblinear']},

'svr':{
          'C':[1.0,2.0,0.2,0.3,0.5,0.9,0.8,3.0],
          'kernel':['linear', 'poly', 'rbf', 'sigmoid'],
          'gamma':['scale', 'auto'],

          'max_iter':range(100,300,50),
          }
}