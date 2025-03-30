import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def show_dashboard(df):
    """Display the full dashboard with enhanced sales analysis."""
    st.title("🎮 Video Game Sales Dashboard")
    st.markdown("**Explore sales performance, trends, and market segments for games with sales > 100,000 copies (vgchartz.com).**")

    # Row 2: Key Metrics
    st.header("1. Sales Performance")
    st.subheader("Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Global Sales", f"{df['Global_Sales'].sum():.2f}M" if not df.empty else "N/A")
    with col2:
        top_game = df.loc[df["Global_Sales"].idxmax()]["Name"] if not df.empty else "N/A"
        st.metric("Top Game", top_game)
    with col3:
        top_publisher = df.groupby("Publisher")["Global_Sales"].sum().idxmax() if not df.empty else "N/A"
        st.metric("Top Publisher", top_publisher)
    with col4:
        top_genre = df.groupby("Genre")["Global_Sales"].sum().idxmax() if not df.empty else "N/A"
        st.metric("Top Genre", top_genre)

    # Row 3: Top 10 Games
    st.subheader("Top 10 Games")
    if not df.empty:
        top_10_games = df.nlargest(10, "Global_Sales")
        fig1 = px.bar(top_10_games, x="Name", y="Global_Sales", title="Top 10 Games by Sales", color="Genre", height=400, 
                      text=top_10_games["Global_Sales"].round(2), hover_data=["Platform", "Year", "Publisher"])
        fig1.update_traces(textposition="outside")
        fig1.update_layout(showlegend=False)
        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.write("No game data available.")

    # Row 4: Platform Insights - Sales Share
    st.header("2. Platform Insights")
    st.subheader("Platform Sales Share")
    if not df.empty:
        top_platforms = df.groupby("Platform")["Global_Sales"].sum().reset_index()
        fig2 = px.treemap(top_platforms, path=["Platform"], values="Global_Sales", title="Platform Sales Share", height=400, 
                          color="Global_Sales", color_continuous_scale="Blues")
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.write("No platform data available.")

    # Row 5: Platform Insights - Platform-Genre Breakdown (Heatmap)
    st.subheader("Platform-Genre Breakdown")
    if not df.empty:
        platform_genre = df.groupby(["Platform", "Genre"])["Global_Sales"].sum().reset_index()
        pivot_table = platform_genre.pivot(index="Platform", columns="Genre", values="Global_Sales").fillna(0)
        fig2b = go.Figure(data=go.Heatmap(z=pivot_table.values, x=pivot_table.columns, y=pivot_table.index, 
                                          colorscale="Blues", text=pivot_table.values.round(2), texttemplate="%{text}M"))
        fig2b.update_layout(title="Sales by Platform and Genre (Heatmap)", height=400)
        st.plotly_chart(fig2b, use_container_width=True)
    else:
        st.write("No platform-genre data available.")

    # Row 6: Publisher Insights - Sales Share
    st.header("3. Publisher Insights")
    st.subheader("Publisher Sales Share")
    if not df.empty:
        top_publishers = df.groupby("Publisher")["Global_Sales"].sum().reset_index()
        fig3 = px.treemap(top_publishers, path=["Publisher"], values="Global_Sales", title="Publisher Sales Share", height=400, 
                          color="Global_Sales", color_continuous_scale="Greens")
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.write("No publisher data available.")

    # Row 7: Publisher Insights - Top Game per Publisher
    st.subheader("Top Game per Publisher")
    if not df.empty:
        top_games_by_pub = df.loc[df.groupby("Publisher")["Global_Sales"].idxmax()][["Publisher", "Name", "Global_Sales"]]
        st.write(top_games_by_pub.sort_values("Global_Sales", ascending=False).head(10))
    else:
        st.write("No publisher-game data available.")

    # Row 8: Sales Trends (Expander)
    with st.expander("4. Sales Trends", expanded=True):
        st.subheader("Global Sales Trend")
        if not df.empty:
            trend_df = df.groupby("Year")["Global_Sales"].sum().reset_index()
            trend_df["Rolling_Avg"] = trend_df["Global_Sales"].rolling(window=3, min_periods=1).mean()
            fig4 = px.line(trend_df, x="Year", y=["Global_Sales", "Rolling_Avg"], title="Global Sales Trend with 3-Year Avg", height=400, 
                           labels={"value": "Sales (M)", "variable": "Metric"})
            fig4.update_traces(mode="lines+markers")
            st.plotly_chart(fig4, use_container_width=True)
        else:
            st.write("No trend data available.")
        
        st.subheader("Genre-Specific Trend")
        if not df.empty:
            genre_trend = df.groupby(["Year", "Genre"])["Global_Sales"].sum().reset_index()
            selected_genre = st.selectbox("Select Genre for Trend", options=genre_trend["Genre"].unique())
            genre_filtered = genre_trend[genre_trend["Genre"] == selected_genre]
            fig5 = px.line(genre_filtered, x="Year", y="Global_Sales", title=f"{selected_genre} Sales Trend", height=400, markers=True)
            st.plotly_chart(fig5, use_container_width=True)
        else:
            st.write("No genre trend data available.")
        
        st.subheader("Regional Sales Trend")
        if not df.empty:
            region_trend = df.groupby("Year")[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].sum().reset_index()
            fig6 = px.area(region_trend, x="Year", y=["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"], title="Regional Sales Trends (Stacked)", height=400)
            st.plotly_chart(fig6, use_container_width=True)
        else:
            st.write("No regional trend data available.")

    # Row 9: Market Segments
    st.header("5. Market Segments")
    st.subheader("Regional Sales Analysis")
    if not df.empty:
        region_sales = df[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].sum().reset_index()
        region_sales.columns = ["Region", "Sales"]
        fig7a = px.bar(region_sales, x="Region", y="Sales", title="Regional Sales Totals", height=400, 
                       color="Region", text=region_sales["Sales"].round(2))
        fig7a.update_traces(textposition="outside")
        st.plotly_chart(fig7a, use_container_width=True)
        
        st.markdown("**Top Genres by Region**")
        region_genre = df.groupby("Genre")[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].sum().reset_index()
        fig7b = px.bar(region_genre.melt(id_vars=["Genre"], value_vars=["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"], 
                                         var_name="Region", value_name="Sales"), 
                       x="Region", y="Sales", color="Genre", title="Sales by Region and Genre", height=400, barmode="group")
        st.plotly_chart(fig7b, use_container_width=True)
    else:
        st.write("No regional data available.")

    st.subheader("Genre-Platform Breakdown")
    if not df.empty:
        genre_platform = df.groupby(["Genre", "Platform"])["Global_Sales"].sum().reset_index()
        fig8 = px.sunburst(genre_platform, path=["Genre", "Platform"], values="Global_Sales", title="Sales by Genre and Platform", height=600)
        st.plotly_chart(fig8, use_container_width=True)
    else:
        st.write("No genre-platform data available.")

    # Row 10: Advanced Insights
    st.header("6. Advanced Insights")
    st.subheader("Regional Sales Correlations")
    if not df.empty:
        region_corr = df[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].corr()
        fig9 = go.Figure(data=go.Heatmap(z=region_corr.values, x=region_corr.columns, y=region_corr.index, 
                                         colorscale="Viridis", text=region_corr.values.round(2), texttemplate="%{text}"))
        fig9.update_layout(title="Correlation Between Regional Sales", height=400)
        st.plotly_chart(fig9, use_container_width=True)
    else:
        st.write("No correlation data available.")

    # Row 11: Raw Data (Expander)
    with st.expander("View Filtered Data", expanded=False):
        if not df.empty:
            st.write(df)
        else:
            st.write("No data matches the selected filters.")

# Optional: Allow standalone execution for testing
if __name__ == "__main__":
    import pandas as pd
    df = pd.read_csv("vgsales.csv")
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    show_dashboard(df)