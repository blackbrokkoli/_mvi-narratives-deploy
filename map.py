from src.map_utils import create_map, create_snapshot

sn1 = create_snapshot(
    name="Keyword Themes",
    subtitle="Clusters of talks linked by shared keywords.",
    summaryImg="https://www.dl.dropboxusercontent.com/s/oocyibrvojcmieg/Screen%20Shot%202020-11-25%20at%207.20.12%20AM.png?dl=0",
    description="hi!",
    layout_params={
        "plotType": "scatterplot",
        "xaxis": "x_tsne",
        "yaxis": "y_tsne",
        "settings": {
            # node size
            "nodeSizeAttr": "views",
            "nodeSizeScaleStrategy": "log", # "linear" or "log"
            "nodeSizeMin": 1,
            "nodeSizeMax": 20,
            "nodeSizeMultiplier": .5,
            "bigOnTop": True,
            # node color and images
            "nodeColorAttr": "keyword_theme",
            "nodeImageShow": True,
            "nodeImageAttr": "photo",
            # link rendering
            "drawEdges": False,
            "edgeCurvature": 0.6,
            "edgeDirectionalRender": "outgoing",
            "edgeSizeStrat": "attr", # or "fixed"
            "edgeSizeAttr": "weight", # size by similarity
            "edgeSizeMultiplier": .7,
            # labels
            "drawGroupLabels": True,
            # layout rendering
            "xAxShow": False,
            "yAxShow": False,
            "scatterAspect": 0.4, # shigher than 0.5 spreads out the scatterplot horizontally
        },
    },
)


# create map
create_map(
    datapointsPath="data_in/nodes.csv",
    linksPath="data_in/links.csv",
    datapointAttrPath="data_in/node_attrs.csv",
    node_attr_map={"OriginalLabel": "label", "OriginalX": "x_tsne", "OriginalY": "y_tsne"},
    link_attr_map={"source": "Source", "target": "Target", "isDirectional": "isDirectional"},
    outFolder="static",
    snapshots=[sn1],
    playerSettings={
        "modalTitle": "10 years of TED talks",
        "modalSubtitle": '<h6>This is a map of every talk on TED.com published from 2007 to 2017.  \
                            Keyword tags for each talk were enhanced by searching through the full transcript of each talk \
                            for the presence of any keyword from the TED\'s tag list, and adding it as a tag if was not already present.</h6>\
                            <h6>Talks are linked if they have high overlap in their tags,  and they self-cluster into groups that \
                            tend to share similar *combinations* of tags. These Keyword Themes are auto-labeled by the 3 most commonly shared tags in the group.</h6>\
                            &#10;&#10;<h6>Data are from a public dataset on <a href="https://www.kaggle.com/rounakbanik/ted-talks/data " target="_blank">Kaggle</a>. \
                            <span>The network was generated using the open source python </span><a href="https://github.com/foodwebster/Tag2Network" target="_blank">\'tag2network\'</a><span> \
                            package, and visualized using <a href="http://openmappr.org" target="_blank">\'openmappr\'</a> - an open source network exploration tool. \
                            <br/></span></h6><h6><p><br/></p><p><i>This visualization is not optimized for mobile viewing and works best in Chrome browsers.   </i><br/></p></h6>',
        "modalDescription": "<h5><span>How to Navigate this Network:</span><br/></h5><ul><li>Click on any node to see more details about that talk and watch the video. \
                            </li><li>Click the '<b>reset</b>' button to clear any selection.</li><li>Use the <b>Snapshots</b> panel to navigate between views.</li>\
                            <li>Use the <b>Filters</b> panel to select talks by any combination of traits (tags, views, event, talk duration, year published, etc).</li>\
                            <li>Click the '<b>Subset</b>' button to restrict the data to the selected nodes. The <b>Filters</b> panel will then summarize that <b>subset</b>. </li>\
                            <li>Use the <b>List</b> panel to see selected or subsetted talks as a sortable list - and to explore their details one by one by clicking on them.  </li></ul>",
    },
)
