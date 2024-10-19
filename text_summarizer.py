from openai import AzureOpenAI
import sys
deployment_name=""
api_key=""
api_endpoint=""
model_name= ""

def get_user_inputs():
    input_file = input("What text file do you want to summarize? ")
    output_file = input("What text file do you want to write the summary to? ")
    num_lines = input("In how many lines do you want to summarize this text? ")

    try:
        num_lines = int(num_lines)
        print("User input received.")
    except ValueError:
        print("The number of lines must be an integer.")
        sys.exit(1)

    return input_file, output_file, num_lines
def read_input_file(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"The file '{input_file}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def summarize_text(input_text, output_file, num_lines):
    try:
        client = AzureOpenAI(
                        api_key=api_key,
                        api_version="2024-02-01",
                        azure_endpoint=api_endpoint
                    )
        prompt = f"Please provide a summary of the following text in {num_lines} lines:\n\n{input_text}"
        response = client.chat.completions.create(
            messages=[{"role": "system", "content": prompt}],
            model=model_name
        )

        summary = response.choices[0].message.content
        return summary

    except Exception as e:
        print(f"Error: {e}")

def write_output_file(output_file, summary):
    try:
        with open(output_file, 'w') as file:
            file.write(summary)
        print(f"Summary successfully written to {output_file}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
        sys.exit(1)

def main():
    try:
        input_file, output_file, num_lines = get_user_inputs()
        input_text = read_input_file(input_file)
        text_summary = summarize_text(input_text, output_file, num_lines)
        write_output_file(output_file, text_summary)
    except Exception as e:
        print(f"Some error occured {e}")

main()




