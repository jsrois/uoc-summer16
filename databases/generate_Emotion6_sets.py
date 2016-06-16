import random
from sys import argv

emotion6_root=argv[1]
input_file=emotion6_root+"/ground_truth.txt"
output_files = { "train" : "em6_posneg_train.txt", "test" : "em6_posneg_test.txt"}
negative_samples = []
positive_samples = []

def write_samples(samples, filename):
    with open(filename, 'w') as out:
        for element in samples:
            out.write(element[0] + ' ' + str(element[1]) +'\n')
    return

# shuffle and split samples into training (80%) and test (20%) sets
with open(input_file) as f:
    next(f) # or store header line with f.readline() instead
    for line in f:
        columns = line.split()
	file_path=emotion6_root+"/images/"+columns[0]
        if float(columns[1]) > 5:
            positive_samples.append((file_path,1))
        else:
            negative_samples.append((file_path,0))



print("total number of labeled images:\n\t positive: %i\n\t negative %i" % (len(positive_samples), len(negative_samples)))
random.shuffle(positive_samples)
random.shuffle(negative_samples)
positives_in_train_set = int(0.8*len(positive_samples))

negatives_in_train_set = int(0.8*len(negative_samples))
print "splitting positives (%i/%i) and negatives (%i/%i)" %(positives_in_train_set,len(positive_samples)-positives_in_train_set,
                                                            negatives_in_train_set,len(negative_samples)-negatives_in_train_set)
train_set = positive_samples[:positives_in_train_set] + negative_samples[:negatives_in_train_set]
test_set  = positive_samples[positives_in_train_set:] + negative_samples[negatives_in_train_set:]
random.shuffle(train_set)
random.shuffle(test_set)

write_samples(train_set, output_files["train"])
write_samples(test_set, output_files["test"])