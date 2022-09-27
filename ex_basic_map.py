from src.map_utils import create_map, create_snapshot

sn1 = create_snapshot(
    name="Keyword Themes",
    subtitle="Clusters of talks linked by shared keywords.",
)



# generate map folder
create_map(
    datapointsPath="data_in/nodes.csv",
    linksPath="data_in/links.csv",
    datapointAttrPath="data_in/node_attrs.csv",
    node_attr_map={"OriginalLabel": "label", "OriginalX": "x_tsne", "OriginalY": "y_tsne"},
    link_attr_map={"source": "Source", "target": "Target", "isDirectional": "isDirectional"},
    outFolder="static",
    snapshots=[sn1]
)
