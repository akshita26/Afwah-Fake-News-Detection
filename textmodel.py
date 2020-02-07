from keras.preprocessing import sequence

from keras.models import model_from_json
from keras.models import load_model

json_file = open('model_num.json', 'r')

loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

# load weights into new model
loaded_model.load_weights("model_num.h5")
#print("Loaded model from disk")

import pickle

with open('words.pickle', 'rb') as handle:
    word_bank = pickle.load(handle)



def predict(test):
	test = test.split()

	i=0
	while i<len(test):
	    #print(test[i])
	    if test[i] in word_bank:
	        test[i] = word_bank[test[i]]
	        i+=1
	    else:
	        del test[i]
	        
	t = []
	t.append(test)

	test1 = sequence.pad_sequences(t, 500)

	out = loaded_model.predict_classes(test1)
	return(int(out))