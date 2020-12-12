
import plotly.graph_objs as go

import pandas as pd
import warnings
warnings.filterwarnings('ignore')
election_data = pd.read_csv(r'president_county_candidate.csv')
# print(election_data)
filter_data = election_data[(election_data['party'] == 'DEM') | (election_data['party'] == 'REP')]

df = pd.pivot_table(filter_data, index=['state', 'party'], values='total_votes', aggfunc=['count', 'sum']).reset_index()
df.columns = ['state', 'party', 'total_votes', 'count']
del df['total_votes']

won_die = list(df["count"])
N = 2
group_ = [won_die[n:n+N] for n in range(0, len(won_die), N)]

list_of_label = list()
for x in group_:
    if x[0] > x[1]:
        label = "red"
    else:
        label = "blue"
    list_of_label.append(label)


dem_count = df[df['party'] == "DEM"]
dm_vote = list(dem_count["count"])
# print(dm_vote)
rep_count = df[df['party'] == "REP"]
rep_vote = list(rep_count["count"])


# import plotly.graph_objects as go
x_ticks = list(set(list(df.state)))

fig = go.Figure()

fig.add_trace(
    # go.Bar(name='DEM', x=animals, y=dm_vote),
    go.Bar(name='REP', x=[x for x in range(0,51) ], y=rep_vote)
)

fig.add_trace(
    go.Bar(name='DEM', x=[x for x in range(0,51) ], y=dm_vote),
    # go.Bar(name='REP', x=animals, y=rep_vote)
)

fig.add_trace(
    go.Scatter(
        mode='markers',
        x=[x for x in range(0,51) ],
        y=[0]*51,
        marker=dict(
            color=list_of_label,
            size=10,

        )

    )
)

fig.update_layout(
    xaxis = dict(
        tickmode = 'array',
        tickvals = [x for x in range(0,51) ],
        ticktext = x_ticks
    )
)


fig.show()