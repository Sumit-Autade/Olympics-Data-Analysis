import streamlit as st
from streamlit_option_menu import option_menu





# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
EXAMPLE_NO = 3


def streamlit_menu(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Projects", "Contact"],  # required
                icons=["house", "book", "envelope"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected

    if example == 2:
        # 2. horizontal menu w/o custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Projects", "Contact"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected

    if example == 3:
        # 2. horizontal menu with custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Projects", "About"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )
        return selected


selected = streamlit_menu(example=EXAMPLE_NO)

if selected == "Home":
    # Page Title
    st.title('Olympics Data Analysis')
    import streamlit as st

   # Olympics Logo Image

    st.sidebar.image('https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Olympic_rings_without_rims.svg/1024px-Olympic_rings_without_rims.svg.png')
    #st.sidebar.image('C:\Users\Sumit\PycharmProjects\demo\venv\ol.png')

    # Olympics History
    st.header('Olympics History')
    st.write(
        'The Olympic Games are an international multi-sport event held every four years, featuring both summer and winter sports competitions. The modern Olympic Games were inspired by the ancient Olympic Games, which were held in Olympia, Greece, from the 8th century BC to the 4th century AD.')
    st.write(
        'The modern Olympic Games were first held in Athens, Greece, in 1896, and have since become the worlds largest sporting event, with athletes from over 200 nations competing in a variety of sports. The Olympic Games are now divided into the Summer Olympics and the Winter Olympics, with the Summer Olympics being held every four years and the Winter Olympics being held every four years, alternating with the Summer Olympics.')
    st.write("The Olympic Games have a rich history and have been the stage for many memorable moments and performances, from Jesse Owens' four gold medals at the 1936 Berlin Olympics to Usain Bolt's world record-breaking runs at the 2008 Beijing Olympics. The Olympic Games have also been the site of political protests and controversies, such as the 1968 Mexico City Olympics, where American athletes raised their fists in a Black Power salute during the medal ceremony.")


    st.write("The ancient Olympics were held in Olympia, Greece, from the 8th century BCE to the 4th century CE. The modern Olympics, which began in 1896, were inspired by the ancient games.")
    st.write("The modern Olympics were created by French educator Baron Pierre de Coubertin, who believed that sports could foster international understanding and peace.")
    st.write("The modern Olympics were created by French educator Baron Pierre de Coubertin, who believed that sports could foster international understanding and peace.")
    st.write("The first modern Olympics were held in Athens, Greece, in 1896. There were only 14 countries represented and 241 athletes, all male.Women were not allowed to compete in the Olympics until the 1900 Games in Paris, France. However, only 22 of the 997 athletes were women.")
    st.write("The Olympics were canceled three times due to world wars: in 1916, 1940, and 1944.")
    st.write("The modern Olympics have been hosted by 23 different cities in 19 countries. The United States has hosted the most Summer Olympics (four), while France has hosted the most Winter Olympics (three).")

    # Data Analysis
    st.header('Data Analysis')
    st.write('Using data from the official Olympic website, I analyze various aspects of the Olympics, including:')
    st.write('- The performance of individual athletes and countries in different events')
    st.write('- Trends and patterns in Olympic performance over time')
    st.write('- The impact of factors such as age, gender, and nationality on Olympic success')





    # Conclusion
    st.write(
        'Thank you for visiting my Olympics Data Analysis project. I hope you enjoy exploring the world of the Olympics!')

if selected == "Projects":

    import pandas as pd
    import preprocessor, helper
    import plotly.express as px
    import matplotlib.pyplot as plt
    import seaborn as sns
    import plotly.figure_factory as ff
    import scipy



    df = pd.read_csv('athlete_events.csv')
    region_df = pd.read_csv('noc_regions.csv')

    df = preprocessor.preprocess(df, region_df)

    st.sidebar.title("Olympics Analysis")
    st.sidebar.image(
        'https://e7.pngegg.com/pngimages/1020/402/png-clipart-2024-summer-olympics-brand-circle-area-olympic-rings-olympics-logo-text-sport.png')
    user_menu = st.sidebar.radio(
        'Select an Option',
        ('Medal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Athletes wise Analysis')
    )

    if user_menu == 'Medal Tally':
        st.sidebar.header("Medal Tally")
        years, country = helper.country_year_list(df)

        selected_year = st.sidebar.selectbox("Select Year", years)
        selected_country = st.sidebar.selectbox("Select Country", country)

        medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)
        if selected_year == 'Overall' and selected_country == 'Overall':
            st.title("Overall Tally")
        if selected_year != 'Overall' and selected_country == 'Overall':
            st.title("Medal Tally in " + str(selected_year) + " Olympics")
        if selected_year == 'Overall' and selected_country != 'Overall':
            st.title(selected_country + " overall performance")
        if selected_year != 'Overall' and selected_country != 'Overall':
            st.title(selected_country + " performance in " + str(selected_year) + " Olympics")
        st.table(medal_tally)

    if user_menu == 'Overall Analysis':
        editions = df['Year'].unique().shape[0] - 1
        cities = df['City'].unique().shape[0]
        sports = df['Sport'].unique().shape[0]
        events = df['Event'].unique().shape[0]
        athletes = df['Name'].unique().shape[0]
        nations = df['region'].unique().shape[0]

        st.title("Top Statistics")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("Editions")
            st.title(editions)
        with col2:
            st.header("Hosts")
            st.title(cities)
        with col3:
            st.header("Sports")
            st.title(sports)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("Events")
            st.title(events)
        with col2:
            st.header("Nations")
            st.title(nations)
        with col3:
            st.header("Athletes")
            st.title(athletes)

        nations_over_time = helper.data_over_time(df, 'region')
        fig = px.line(nations_over_time, x="count", y="region")
        st.title("Participating Nations over the years")
        st.plotly_chart(fig)

        events_over_time = helper.data_over_time(df, 'Event')
        fig = px.line(events_over_time, x="Edition", y="Event")
        st.title("Events over the years")
        st.plotly_chart(fig)

        athlete_over_time = helper.data_over_time(df, 'Name')
        fig = px.line(athlete_over_time, x="Edition", y="Name")
        st.title("Athletes over the years")
        st.plotly_chart(fig)

        st.title("No. of Events over time(Every Sport)")
        fig, ax = plt.subplots(figsize=(20, 20))
        x = df.drop_duplicates(['Year', 'Sport', 'Event'])
        ax = sns.heatmap(
            x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),
            annot=True)
        st.pyplot(fig)

        st.title("Most successful Athletes")
        sport_list = df['Sport'].unique().tolist()
        sport_list.sort()
        sport_list.insert(0, 'Overall')

        selected_sport = st.selectbox('Select a Sport', sport_list)
        x = helper.most_successful(df, selected_sport)
        st.table(x)

    if user_menu == 'Country-wise Analysis':
        st.sidebar.title('Country-wise Analysis')

        
        temp_df = df.dropna(subset=['Medal'])
        temp_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)

        country_list = temp_df['region'].dropna().unique().tolist()
        country_list.sort()

        selected_country = st.sidebar.selectbox('Select a Country', country_list)

        country_df = helper.yearwise_medal_tally(df, selected_country)
        fig = px.line(country_df, x="Year", y="Medal")
        st.title(selected_country + " Medal Tally over the years")
        st.plotly_chart(fig)

        st.title(selected_country + " excels in the following sports")
        pt = helper.country_event_heatmap(df, selected_country)
        fig, ax = plt.subplots(figsize=(20, 20))
        ax = sns.heatmap(pt, annot=True)
        st.pyplot(fig)

        st.title("Top 10 athletes of " + selected_country)
        top10_df = helper.most_successful_country(df, selected_country)
        st.table(top10_df)

    if user_menu == 'Athletes wise Analysis':
        athlete_df = df.drop_duplicates(subset=['Name', 'region'])

        x1 = athlete_df['Age'].dropna()
        x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
        x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
        x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

        fig = ff.create_distplot([x1, x2, x3, x4],
                                 ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],
                                 show_hist=False, show_rug=False)
        fig.update_layout(autosize=False, width=1000, height=600)
        st.title("Distribution of Age")
        st.plotly_chart(fig)

        x = []
        name = []
        famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                         'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                         'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                         'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                         'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                         'Tennis', 'Golf', 'Softball', 'Archery',
                         'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                         'Rhythmic Gymnastics', 'Rugby Sevens',
                         'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
        for sport in famous_sports:
            temp_df = athlete_df[athlete_df['Sport'] == sport]
            x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
            name.append(sport)

        fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
        fig.update_layout(autosize=False, width=1000, height=600)
        st.title("Distribution of Age wrt Sports(Gold Medalist)")
        st.plotly_chart(fig)

        sport_list = df['Sport'].unique().tolist()
        sport_list.sort()
        sport_list.insert(0, 'Overall')

        st.title('Height Vs Weight')
        selected_sport = st.selectbox('Select a Sport', sport_list)
        temp_df = helper.weight_v_height(df, selected_sport)
        fig, ax = plt.subplots()
        ax = sns.scatterplot(x=temp_df['Weight'], y=temp_df['Height'], hue=temp_df['Medal'], style=temp_df['Sex'], s=60)
        st.pyplot(fig)

        st.title("Men Vs Women Participation Over the Years")
        final = helper.men_vs_women(df)
        fig = px.line(final, x="Year", y=["Male", "Female"])
        fig.update_layout(autosize=False, width=1000, height=600)
        st.plotly_chart(fig)

if selected == "About":

    st.subheader('Medal Tally')
    st.write('The Medal Tally Analysis provides a comprehensive overview of the performance of countries in the Olympics. It quantifies the success of each nation based on the number of gold, silver, and bronze medals won.')
    st.write('key findings:')
    st.write("Over the years, there has been a notable trend in the distribution of gold, silver, and bronze medals among countries.")
    st.write("Certain nations consistently dominate specific sports, while others exhibit a more diverse performance across disciplines.")
    st.write("The analysis also reveals patterns in the total medal count, with some countries consistently ranking at the top, while others show fluctuations")
    st.subheader("Overall Analysis")
    st.write("The Overall Analysis delves into broader trends and patterns across the Olympics, encompassing aspects such as participation rates, host country impact, and demographic shifts.")
    st.write('key findings:')
    st.write("Participation rates in the Olympics have shown a consistent upward trend, reflecting the global growth of interest in sports.")
    st.write("Host countries often experience a surge in performance, known as the 'host nation advantage', with an increase in both medal count and overall competitiveness.")
    st.write("The analysis also sheds light on demographic shifts in Olympic participation, with trends in gender representation and age distributions.")
    st.subheader('Country-wise Analysis')
    st.write("The Country Wise Analysis focuses on specific nations and their performance in the Olympics")
    st.write('key findings:')
    st.write("Some countries has consistently been a powerhouse in specific sports, demonstrating a dominant presence in the Olympic arena.")
    st.write("Economic factors, government investment, and cultural emphasis on sports have played a significant role in shaping the performance of countries.")
    st.write("Notable athletes from some country have contributed significantly to the nation's success.")
    st.subheader('Atheletes-wise Analysis')
    st.write("The Athlete Demographics and Performance Trends section delves into individual athletes' characteristics and their performance trends in the Olympic arena. This analysis offers valuable insights into the age distribution, gender representation, and performance trajectory of athletes.")
    st.write('key findings:')
    st.write("The Athlete Demographics and Performance Trends analysis offers a detailed examination of the characteristics and achievements of Olympic athletes. It provides a nuanced understanding of age distribution, gender representation, and the impact of age on medal success. These insights contribute to a broader appreciation of the diverse and dynamic nature of elite-level competition")
