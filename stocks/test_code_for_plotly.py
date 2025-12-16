
        dates = [
                "2023-01-01",
                "2023-02-01",
                "2023-03-01",
                "2023-04-01",
            ]

        investment = [1000, 1200, 1300, 1500]
        profits = [0, 50, 120, 300]

        # 2️⃣ Δημιουργία γραμμών
        trace_investment = go.Scatter(
            x=dates,
            y=investment,
            mode="lines",
            name="Επένδυση"
        )

        trace_profits = go.Scatter(
            x=dates,
            y=profits,
            mode="lines",
            name="Κέρδη"
        )

        # 3️⃣ Layout (τίτλοι κτλ)
        layout = go.Layout(
            title="Επένδυση & Κέρδη",
            xaxis=dict(title="Ημερομηνία"),
            yaxis=dict(title="Ποσό (€)")
        )

        # 4️⃣ Φτιάχνουμε το figure
        fig = go.Figure(data=[trace_investment, trace_profits], layout=layout)

        # 5️⃣ Μετατροπή σε HTML (ΠΟΛΥ ΣΗΜΑΝΤΙΚΟ)
        plot_div = plot(fig, output_type="div", include_plotlyjs=False)
