from pathlib import Path
import os, sys

SCRIPT_PATH = Path(os.path.realpath(__file__))
PROJECT_DIR = Path(os.path.dirname(os.path.dirname(os.path.dirname(SCRIPT_PATH))))
sys.path.append(str(PROJECT_DIR))

import argparse
import json
from pprint import pprint
from typing import Any, Dict
import pandas as pd
import numpy as np


from snorkel.labeling.model import LabelModel


def train_label_model(args) -> Dict[str, Any]:
    stats: Dict[str, Any] = {}

    train_filename = PROJECT_DIR / args.dataset_path_train
    test_filename = PROJECT_DIR / args.dataset_path_test

    df_train = pd.read_csv(train_filename, sep=';', index_col=0, nrows=args.rows_train)
    df_test = pd.read_csv(test_filename, sep=';', index_col=0, nrows=args.rows_test)

    L_dev = np.load(PROJECT_DIR / args.path_to_heuristics_matrix_train, allow_pickle=True)
    L_test = np.load(PROJECT_DIR / args.path_to_heuristics_matrix_test, allow_pickle=True)

    label_model = LabelModel(cardinality=2, verbose=True)
    label_model.fit(L_train=L_dev, n_epochs=2000, log_freq=100, seed=123)
    label_model.save(PROJECT_DIR / args.save_label_model_to)
    label_model.eval()
    stats['label_model_train_acc'] = label_model.score(L=L_dev, Y=df_train.label, tie_break_policy="random")["accuracy"]
    stats['label_model_test_acc'] = label_model.score(L=L_test, Y=df_test.label, tie_break_policy="random")["accuracy"]
    return stats


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset-path-train', default='data/combination/Training_Dataset.csv')
    parser.add_argument('--dataset-path-test', default='data/combination/Test_Dataset.csv')
    parser.add_argument('--rows-train', type=int, default=50000)
    parser.add_argument('--rows-test', type=int, default=5000)
    parser.add_argument('--path-to-heuristics-matrix-train', default='generated/heuristic_matrix_train.pkl')
    parser.add_argument('--path-to-heuristics-matrix-test', default='generated/heuristic_matrix_test.pkl')
    parser.add_argument('--save-label-model-to', default='generated/label_model.pkl')
    parser.add_argument('--save-metrics-to', default='label_model_metrics.json')
    args = parser.parse_args()

    stats = train_label_model(args)

    with open(PROJECT_DIR / Path(args.save_metrics_to), 'w') as f:
        json.dump(stats, f)

    pprint(stats)