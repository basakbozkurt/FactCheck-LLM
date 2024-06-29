import argparse
import json

import evaluate


def generate_metrics(base_model_name):
    result_file_path = f'data/results_{base_model_name}.json'
    results_file = open(result_file_path, 'r')
    # reference
    refs = []
    # predictions
    preds = []
    # reference in binary mode
    binary_refs = []
    # binary mode predictions
    binary_preds = []
    s = set()

    classes = {'**mostly-false**': '2',
               ':-mostly-false': '2',
               '=-mostly-true': '4',
               'false': '1',
               'half-true': '3',
               'i-cannot-provide-a-fact-checking-evaluation-for-the-given-statement-as-it-contains-offensive-and-defamatory-language-towards-a-person-based-on-their-race.': 'X',
               'mostly-false': '2',
               'mostly-true': '4',
               'mostly-true-with-an-important-clarification.': '4',
               'pants-fire': '0',
               'pants-on-fire': '0',
               'true': '5',
               'inconclusive': 'X'}
    binary_classes = {'**mostly-false**': '0',
                      ':-mostly-false': '0',
                      '=-mostly-true': '1',
                      'false': '0',
                      'half-true': '1',
                      'i-cannot-provide-a-fact-checking-evaluation-for-the-given-statement-as-it-contains-offensive-and-defamatory-language-towards-a-person-based-on-their-race.': 'X',
                      'mostly-false': '0',
                      'mostly-true': '1',
                      'mostly-true-with-an-important-clarification.': '1',
                      'pants-fire': '0',
                      'pants-on-fire': '0',
                      'true': '1'}
    for line in results_file:
        j = json.loads(line)
        prediction = j["prediction"]
        if "mostly false" in prediction:
            prediction = "mostly false"
        elif "mostly true" in prediction:
            prediction = "mostly true"
        elif "half true" in prediction:
            prediction = "half true"
        elif "pants on fire" in prediction:
            prediction = "pants on fire"
        elif "inconclusive" in prediction:
            prediction = "inconclusive"
        elif prediction == "true" or '"true"' in prediction or '**label:** true' in prediction or "abel true" in prediction or "abel: true" in prediction or "**true**" in prediction or "as true" in prediction or "label of true" in prediction:
            prediction = "true"
        elif prediction == "false" or "as false" in prediction or "abel false" in prediction or '"false"' in prediction or 'abel: false' in prediction or "**false**" in prediction or "label of false" in prediction or \
                "i would assign the label false" in prediction or '**label:** false' in prediction or 'statement is false' in prediction:
            prediction = "false"
        elif "*000*" in prediction:
            prediction = prediction.split("**")[1].strip()
        else:
            # ignore this prediction because output is not valid.
            continue
        if j["statement"] in s:
            # this must not happen. just to be sure
            raise Exception(
                "this statement already had been predicted. duplicate records exists. %s" % (j["statement"]))

        s.add(j["statement"])

        prediction = prediction.strip().replace(" ", "-")
        verdict = j["verdict"]

        if classes[verdict] == "X" or classes[prediction] == "X":
            continue
        refs.append(int(classes[verdict]))
        preds.append(int(classes[prediction]))

        # binary mode
        binary_refs.append(int(binary_classes[verdict]))
        binary_preds.append(int(binary_classes[prediction]))
    accuracy_metric = evaluate.load("accuracy")
    accuracy_results = accuracy_metric.compute(references=refs, predictions=preds)
    binary_accuracy_results = accuracy_metric.compute(references=binary_refs, predictions=binary_preds)
    f1_metric = evaluate.load("f1")
    f1_results = f1_metric.compute(references=refs, predictions=preds, average='macro')
    f1_results_binary = f1_metric.compute(references=binary_refs, predictions=binary_preds, average='binary')
    return {
        'accuracy': {'multiclass': accuracy_results, 'binary': binary_accuracy_results},
        'f1': {'multiclass': f1_results, 'binary': f1_results_binary},
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Model Parameter")
    parser.add_argument("model_name", nargs="?", type=str, help="Ollama model name", default="qwen2")

    args = parser.parse_args()
    print(f"The parameter is: '{args.model_name}'")
    metrics = generate_metrics(args.model_name)
    for metric_type in metrics:
        print(metric_type, metrics[metric_type])
        print("---")
