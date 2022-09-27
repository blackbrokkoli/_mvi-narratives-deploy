from src.map_utils import create_map, create_snapshot
import pandas as pd
import numpy as np

# generate x and y for nodes
df = pd.read_csv('data_in/nodes.csv')
# for all rows where 'x_tsne' is empty, fill with a random value between 0 and 40
df['x_tsne'] = df['x_tsne'].fillna(pd.Series(np.random.uniform(0, 170, size=len(df))))
# for all rows where 'y_tsne' is empty, fill with a random value between 0 and 30
df['y_tsne'] = df['y_tsne'].fillna(pd.Series(np.random.uniform(20, 80, size=len(df))))
# save the new dataframe to a csv file
df.to_csv('data_in/nodesWithCoords.csv', index=False)

sn1 = create_snapshot(
    name="Our Narratives",
    subtitle="Explore the MVI's work.",
)


# generate map folder
create_map(
    datapointsPath="data_in/nodesWithCoords.csv",
    linksPath="data_in/links.csv",
    datapointAttrPath="data_in/node_attrs.csv",
    node_attr_map={"OriginalLabel": "label", "OriginalX": "x_tsne", "OriginalY": "y_tsne"},
    link_attr_map={"source": "Source", "target": "Target", "isDirectional": "isDirectional"},
    outFolder="static",
    snapshots=[sn1]
)
