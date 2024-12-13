from hpc_run.dataloader import load_and_split_data, get_feature_target_names
from hpc_run.modeltrainer import find_neighbours
from tqdm.auto import tqdm


def main(dataloc: str):
    # get the train and test datasets
    traindata, testdata = load_and_split_data(dataloc)

    features, target = get_feature_target_names()
    
    labels = []
    for i, row in tqdm(testdata.iterrows(), total=len(testdata), desc="Processing the test dataset"):
        ids = find_neighbours(row[features].values.reshape(1, -1), traindata[features])
        
        labels.append(traindata.loc[ids[0], target].mode()[0])


if __name__== "__main__":
    dataloc = "datasets/creditcard_2023.csv"
    main(dataloc)

