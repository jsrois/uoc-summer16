import random
from sys import argv

def write_samples(samples, filename):
    with open(filename, 'w') as out:
        for element in samples:
            out.write(element[0] + ' ' + str(element[1]) +'\n')
    return

def parse_line(line):
    columns = line.split()
    # todo: include emotion probabilities
    keys   = ['file_path', 'valence', 'arousal']
    values = [columns[0], columns[1], columns[2]]
    return dict(zip(keys,values))

def parse_ground_truth_data(input_file):
    samples=[]
    with open(input_file) as f:
        next(f) # or store header line with f.readline() instead
        for line in f:
            samples.append(parse_line(line))
    return samples

def generate_samples_valence(samples,root_path=''):
    print "Generating samples for regression using valence scores"
    score_samples=[]
    for sample in samples:
        file_path = root_path + "/" + sample['file_path']
        score_samples.append((file_path, sample['valence']))
    random.shuffle(score_samples)
    samples_in_train_set = int(0.8*len(score_samples))
    train_set = score_samples[:samples_in_train_set]
    test_set  = score_samples[samples_in_train_set:]
    write_samples(train_set, "databases/Emotion6/em6_valence_train.txt")
    write_samples(test_set, "databases/Emotion6/em6_valence_test.txt")

def generate_samples_thresholded_valence(samples,root_path=''):
    print "Generating Positive/Negative samples for classification using thresholded valence scores"
    positive_samples=[]
    negative_samples=[]
    for sample in samples:
        file_path=root_path+"/"+sample['file_path']
        if float(sample['valence'])<5:
            negative_samples.append((file_path,0))
        else:
            positive_samples.append((file_path,1))

    print("total number of labeled images:\n\t positive: %i\n\t negative %i" % (len(positive_samples), len(negative_samples)))
    random.shuffle(positive_samples)
    random.shuffle(negative_samples)
    # shuffle and split samples into training (80%) and test (20%) sets
    positives_in_train_set = int(0.8*len(positive_samples))

    negatives_in_train_set = int(0.8*len(negative_samples))
    print "splitting positives (%i/%i) and negatives (%i/%i)" %(positives_in_train_set,len(positive_samples)-positives_in_train_set,
                                                                negatives_in_train_set,len(negative_samples)-negatives_in_train_set)
    train_set = positive_samples[:positives_in_train_set] + negative_samples[:negatives_in_train_set]
    test_set  = positive_samples[positives_in_train_set:] + negative_samples[negatives_in_train_set:]
    random.shuffle(train_set)
    random.shuffle(test_set)

    write_samples(train_set, "databases/Emotion6/em6_posneg_train.txt")
    write_samples(test_set, "databases/Emotion6/em6_posneg_test.txt")



emotion6_root=argv[1]
input_file=emotion6_root+"/ground_truth.txt"

samples = parse_ground_truth_data(input_file)
generate_samples_valence(samples, emotion6_root+'/images')
generate_samples_thresholded_valence(samples, emotion6_root+'/images')

