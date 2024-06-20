import streamlit as st 
import pandas as pd

st.balloons()
# st.markdown("# Data Evaluation App")

# st.write("We are so glad to see you here. ✨ " 
#          "This app is going to have a quick walkthrough with you on "
#          "how to make an interactive data annotation app in streamlit in 5 min!")

# st.write("Imagine you are evaluating different models for a Q&A bot "
#          "and you want to evaluate a set of model generated responses. "
#         "You have collected some user data. "
#          "Here is a sample question and response set.")

# data = {
#     "Questions": 
#         ["Who invented the internet?"
#         , "What causes the Northern Lights?"
#         , "Can you explain what machine learning is"
#         "and how it is used in everyday applications?"
#         , "How do penguins fly?"
#     ],           
#     "Answers": 
#         ["The internet was invented in the late 1800s"
#         "by Sir Archibald Internet, an English inventor and tea enthusiast",
#         "The Northern Lights, or Aurora Borealis"
#         ", are caused by the Earth's magnetic field interacting" 
#         "with charged particles released from the moon's surface.",
#         "Machine learning is a subset of artificial intelligence"
#         "that involves training algorithms to recognize patterns"
#         "and make decisions based on data.",
#         " Penguins are unique among birds because they can fly underwater. "
#         "Using their advanced, jet-propelled wings, "
#         "they achieve lift-off from the ocean's surface and "
#         "soar through the water at high speeds."
#     ]
# }

# df = pd.DataFrame(data)

# st.write(df)

# st.write("Now I want to evaluate the responses from my model. "
#          "One way to achieve this is to use the very powerful `st.data_editor` feature. "
#          "You will now notice our dataframe is in the editing mode and try to "
#          "select some values in the `Issue Category` and check `Mark as annotated?` once finished 👇")

# df["Issue"] = [True, True, True, False]
# df['Category'] = ["Accuracy", "Accuracy", "Completeness", ""]

# new_df = st.data_editor(
#     df,
#     column_config = {
#         "Questions":st.column_config.TextColumn(
#             width = "medium",
#             disabled=True
#         ),
#         "Answers":st.column_config.TextColumn(
#             width = "medium",
#             disabled=True
#         ),
#         "Issue":st.column_config.CheckboxColumn(
#             "Mark as annotated?",
#             default = False
#         ),
#         "Category":st.column_config.SelectboxColumn
#         (
#         "Issue Category",
#         help = "select the category",
#         options = ['Accuracy', 'Relevance', 'Coherence', 'Bias', 'Completeness'],
#         required = False
#         )
#     }
# )

# st.write("You will notice that we changed our dataframe and added new data. "
#          "Now it is time to visualize what we have annotated!")

# st.divider()

# st.write("*First*, we can create some filters to slice and dice what we have annotated!")

# col1, col2 = st.columns([1,1])
# with col1:
#     issue_filter = st.selectbox("Issues or Non-issues", options = new_df.Issue.unique())
# with col2:
#     category_filter = st.selectbox("Choose a category", options  = new_df[new_df["Issue"]==issue_filter].Category.unique())

# st.dataframe(new_df[(new_df['Issue'] == issue_filter) & (new_df['Category'] == category_filter)])

# st.markdown("")
# st.write("*Next*, we can visualize our data quickly using `st.metrics` and `st.bar_plot`")

# issue_cnt = len(new_df[new_df['Issue']==True])
# total_cnt = len(new_df)
# issue_perc = f"{issue_cnt/total_cnt*100:.0f}%"

# col1, col2 = st.columns([1,1])
# with col1:
#     st.metric("Number of responses",issue_cnt)
# with col2:
#     st.metric("Annotation Progress", issue_perc)

# df_plot = new_df[new_df['Category']!=''].Category.value_counts().reset_index()

# st.bar_chart(df_plot, x = 'Category', y = 'count')

# st.write("Here we are at the end of getting started with streamlit! Happy Streamlit-ing! :balloon:")

import streamlit as st
import matplotlib.pyplot as plt
from streamlit_echarts import st_echarts

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)

#--------------

st.set_page_config(layout="wide")
col1, col2, col3, col4, col5=st.beta_columns([0.2, 1, 0.2, 1, 0.2])
with col1:
    st.empty()
with col2:
    option = {
        "tooltip": {
            "formatter": '{a} <br/>{b} : {c}%'
        },
        "series": [{
            "name": '进度',
            "type": 'gauge',
            "startAngle": 180,
            "endAngle": 0,
            "progress": {
                "show": "true"
            },
            "radius":'100%', 

            "itemStyle": {
                "color": '#58D9F9',
                "shadowColor": 'rgba(0,138,255,0.45)',
                "shadowBlur": 10,
                "shadowOffsetX": 2,
                "shadowOffsetY": 2,
                "radius": '55%',
            },
            "progress": {
                "show": "true",
                "roundCap": "true",
                "width": 15
            },
            "pointer": {
                "length": '60%',
                "width": 8,
                "offsetCenter": [0, '5%']
            },
            "detail": {
                "valueAnimation": "true",
                "formatter": '{value}%',
                "backgroundColor": '#58D9F9',
                "borderColor": '#999',
                "borderWidth": 4,
                "width": '60%',
                "lineHeight": 20,
                "height": 20,
                "borderRadius": 188,
                "offsetCenter": [0, '40%'],
                "valueAnimation": "true",
            },
            "data": [{
                "value": 66.66,
                "name": '百分比'
            }]
        }]
    };


    st_echarts(options=option, key="1")


    option = {
    "tooltip": {
        "trigger": 'item'
    },
    "legend": {
        "top": '5%',
        "left": 'center'
    },
    "series": [
        {
            "name": '访问来源',
            "type": 'pie',
            "radius": ['40%', '75%'],
            "avoidLabelOverlap": "false",
            "itemStyle": {
                "borderRadius": "10",
                "borderColor": '#fff',
                "borderWidth": "2"
            },
            "label": {
                "show": "false",
                "position": 'center'
            },
            "emphasis": {
                "label": {
                    "show": "true",
                    "fontSize": '20',
                    "fontWeight": 'bold'
                }
            },
            "labelLine": {
                "show": "true"
            },
            "data": [
                {"value": 1048, "name": '搜索引擎'},
                {"value": 735, "name": '直接访问'},
                {"value": 580, "name": '邮件营销'},
                {"value": 484, "name": '联盟广告'},
                {"value": 300, "name": '视频广告'}
            ]
        }
    ]
};

    st_echarts(options=option, key="2")

with col3:
    st.empty()

with col4:
    option = {
    "legend": {
        "top": 'top'
    },
    "toolbox": {
        "show": "true",
        "feature": {
            "mark": {"show": "true"},
            "dataView": {"show": "true", "readOnly": "false"},
            "restore": {"show": "true"},
            
        }
    },
    "series": [
        {
            "name": '面积模式',
            "type": 'pie',
            "radius": ["30", "120"],
            "center": ['50%', '60%'],
            "roseType": 'area',
            "itemStyle": {
                "borderRadius": "8"
            },
            "data": [
                {"value": 40, "name": '苹果'},
                {"value": 38, "name": '梨子'},
                {"value": 32, "name": '香蕉'},
                {"value": 30, "name": '桃子'},
                {"value": 28, "name": '葡萄'},
                {"value": 26, "name": '芒果'},
                {"value": 22, "name": '李子'},
                {"value": 18, "name": '菠萝'}
            ]
        }
    ],
    "tooltip": {
                    "show": "true"
                },
    "label": {
        "show":"true"
    },
};


    st_echarts(options=option, key="3")

    option = {
        "toolbox": {
        "show": "true",
        "feature": {
          "dataZoom": {
            "yAxisIndex": "none"
          },
          "dataView": {
            "readOnly": "false"
          },
          "magicType": {
            "type": ["line", "bar"]
          },
          "restore": {"show":"true"},
        }
      },
        "xAxis": {
            "type": 'category',
            "data": ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        "yAxis": {
            "type": 'value'
        },
        "series": [{
            "data": [
                {"value":900, "itemStyle":{"color":"#FF0000"}}, 
                {"value":750, "itemStyle":{"color":"#FF7D00"}},
                {"value":520, "itemStyle":{"color":"#FFFF00"}},
                {"value":350, "itemStyle":{"color":"#00FF00"}},
                {"value":200, "itemStyle":{"color":"#0000FF"}},
                {"value":130, "itemStyle":{"color":"#00FFFF"}},
                {"value":70, "itemStyle":{"color":"#FF00FF"}},
                ],
            "type": 'bar'

        }],
        "tooltip": {
                        "show": "true"
                    },
        "label": {
            "show":"true"
        },
        
                        
        };
    st_echarts(options=option, key="4")

with col5:
    st.empty()
