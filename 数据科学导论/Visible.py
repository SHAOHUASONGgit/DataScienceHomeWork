from pyecharts.charts import Radar
from pyecharts.charts import WordCloud
from pyecharts import options as opts
from pyecharts.charts import HeatMap

#雷达图
dataOne = [[10, 6, 6, 10, 2]]
radar = (
    Radar()
        .add_schema(
        schema=[
            {
                "name": "Hadoop", "max": 12, "min": 0, "color": 'black', "font_size": 18},
            {
                "name": "BigData", "max": 12, "min": 0, "color": 'black', "font_size": 18},
            {
                "name": "NoSQL", "max": 12, "min": 0, "color": 'black', "font_size": 18},
            {
                "name": "DataBase", "max": 12, "min": 0, "color": 'black', "font_size": 18},
            {
                "name": "CloudComputing", "max": 12, "min": 0, "color": 'black', "font_size": 18},
        ], shape='circle'
    )
        .add('相关文章数量', dataOne, color='blue')
        .set_global_opts(title_opts=opts.TitleOpts(title='雷达图'), )
)
radar.render('雷达图.html')

#词云
dataTwo = [('Hadoop',7),('NoSQL',8),('guide',3),('Data',6),('definitive',2),('fast',2),('Apache',1),('architecture',1),('Big',1),('Cassandra',1),('CouchDB',1),('Getting',1),('Google',1),('Making',1),('MapReduce',1),('MongoDB',1),('Oracle',1),('Pro',1),('Professional',1),('Redis',1),('Yarn',1),('ZooKeeper',1),('Action',2),('Advanced',1),('analytics',1),('brief',1),('Clusters',2)]
wordcloud = WordCloud()
wordcloud.add('', dataTwo, shape='diamond')
wordcloud.render('词云.html')

#热力图
value = [[0,0,0],[0,1,0],[0,2,0],[0,3,0],[0,4,25],
         [1,0,25],[1,1,25],[1,2,0],[1,3,0],[1,4,25],
         [2,0,25],[2,1,0],[2,2,0],[2,3,0],[2,4,0],
         [3,0,25],[3,1,0],[3,2,0],[3,3,50],[3,4,0],
         [4,0,0],[4,1,0],[4,2,25],[4,3,75],[4,4,0],
         [5,0,50],[5,1,0],[5,2,25],[5,3,25],[5,4,0],
         [6,0,50],[6,1,75],[6,2,100],[6,3,50],[6,4,25],
         [7,0,0],[7,1,25],[7,2,25],[7,3,25],[7,4,0],
         [8,0,75],[8,1,50],[8,2,25],[8,3,25],[8,4,0],
         [9,0,0],[9,1,0],[9,2,0],[9,3,0],[9,4,25],
         [11,0,25],[11,1,25],[11,2,0],[11,3,0],[11,4,0]]
heatmap = (
    HeatMap()
    .add_xaxis([2003,2004,2009,2010,2011,2012.2013,2014,2015,2016,2017])
    .add_yaxis(
        "",
        ['Hadoop','BigData','NoSQL','DataBase','CloudComputing'],
        value,
        label_opts=opts.LabelOpts(is_show=True, position="inside"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="文献研究方向热力图"),
        visualmap_opts=opts.VisualMapOpts(),
    )
)
heatmap.render("热力图.html")