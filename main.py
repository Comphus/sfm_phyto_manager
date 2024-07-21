import json

# Load the phyto_helper_data.json file
with open("phyto_helper_data.json") as file:
    phyto_factory_data = json.load(file)

    
# Apply seeds to template
def construct_seed_text(seed_template : str, seed : str) -> str:
    return seed_template.format(seed=seed)


def main() -> str:
    # assign the values from the phyto_helper_data.json file to variables
    base_factory_text = phyto_factory_data["base_text"]
    base_seed_template = phyto_factory_data["seed_text_template"]
    seed_keyword_exceptions = phyto_factory_data["keyword_exceptions"]
    exception_base_seed_template = phyto_factory_data["exception_seed_text_template"]
    seeds = phyto_factory_data["seeds"]
    # initialize variables
    final_seed_list = []
    final_seed_text = ""
    final_factory_text = ""

    # loop through all seeds in the seeds list and apply them to the seed template
    for seed in seeds:
        seed_text = construct_seed_text(
            base_seed_template if seed not in seed_keyword_exceptions else exception_base_seed_template,
            seed
        )
        final_seed_list.append(seed_text)

    # combine final results into a single string
    final_seed_text = "\n".join(final_seed_list)
    final_factory_text = base_factory_text + final_seed_text

    # write results to a file
    with open("seed_output.txt", "w") as output_file:
        output_file.write(final_factory_text)
    return final_factory_text


if __name__ == "__main__":
    print(main())
