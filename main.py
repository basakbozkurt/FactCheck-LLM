import ollama, json, hashlib


def remove_double_quotes(statement):
    if statement:
        return statement.replace('"', '')
    return statement


base_model = 'llama3'

model_from = f'FROM {base_model}'
system_prompt = '''SYSTEM """You are a fact-checking expert. Evaluate the given statement and assign one of the following labels:
TRUE – The statement is accurate and nothing significant is missing.
MOSTLY TRUE – The statement is accurate but requires clarification or additional information.
HALF TRUE – The statement is partially accurate but omits important details or takes things out of context.
MOSTLY FALSE – The statement contains some truth but ignores critical facts that would provide a different impression.
FALSE – The statement is not accurate.
PANTS ON FIRE – The statement is not accurate and makes a ridiculous claim.
INCONCLUSIVE – A clear decision cannot be made due to insufficient context or information.

Provide the assigned {label} along with a detailed {explanation} supporting your assessment."""
'''

modelfile = model_from + '\n' + system_prompt

file_path = 'data/politifact_factcheck_data_sampled.json'
model_name = base_model + "_fact"
ollama.create(model=model_name, modelfile=modelfile)

output_file = f'data/results_{base_model}.json'

write_file = open(output_file, "a")
result_set = set()

with open(write_file, 'r') as r:
    for line in r:
        j = json.loads(line)
        result_set.add(hashlib.sha256(j["statement"].encode("utf8")).hexdigest())

with open(file_path, 'r') as file:
    for line in reversed(file.readlines()):
        data = json.loads(line.strip())

        # Extract the necessary fields
        statement = data.get('statement')
        statement_originator = data.get('statement_originator')
        statement_date = data.get('statement_date')
        statement = remove_double_quotes(statement)
        if hashlib.sha256(data["statement"].encode("utf8")).hexdigest() in result_set:
            # this statement already in output file
            # to allow continue without duplication when failed
            continue
        print("----")
        formatted_statement = f'Statement: "{statement}" made by {statement_originator} on {statement_date}.'
        r = ollama.generate(model=model_name, prompt=formatted_statement)
        v = r["response"].split("\n")[0].strip()
        v = v.strip("{Label}:").strip().lower()
        data["prediction"] = v
        print(v, data["verdict"], formatted_statement)
        write_file.write(json.dumps(data) + "\n")
        write_file.flush()
        print("----")
