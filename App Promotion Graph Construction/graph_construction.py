import pandas as pd
import ast

# Load the CSV file

def get_links_nodes():
    file_path = '../data/R5CT90DQDVR_2023.12.31-22.18.49_dfs_greedy-random.csv'
    df = pd.read_csv(file_path)

    # Convert string representation of list in 'ad' column to actual list
    df['ad'] = df['ad'].apply(ast.literal_eval)

    # Creating the link table
    link_data = []
    for index, row in df.iterrows():
        pkg_src = row['pkg_name']
        for pkg_dst in row['ad']:
            link_data.append({'pkg_src': pkg_src, 'pkg_dst': pkg_dst})

    link_table = pd.DataFrame(link_data)

    # Removing invalid entries from the link table
    invalid_entry = "Broadcasting: Intent { act=clipper.get flg=0x400000 }\nBroadcast completed: result=0, data="
    link_table_cleaned = link_table[~link_table['pkg_dst'].str.contains(invalid_entry, na=False)]

    # Creating the node table with unique package names
    unique_pkg_names = set(link_table_cleaned['pkg_src']).union(set(link_table_cleaned['pkg_dst']))
    node_table_cleaned = pd.DataFrame({'pkg_names': list(unique_pkg_names)})

    node_table_cleaned.to_csv('../data/nodes.csv')
    link_table_cleaned.to_csv('../data/links.csv')

