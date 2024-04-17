queries = [
    {
        "name": "query1AllegationsTypes",
        "csv_path": "DatasetForPrivacy/bpd-allegations.csv",
        "meta_path": "DatasetForPrivacy/bpd-allegations.yaml",
        "query": """
            SELECT allegation, COUNT(*) AS frequency
            FROM bpd_allegations.bpd_allegations
            GROUP BY allegation
            ORDER BY frequency DESC;
        """,
        # "epsilon_range": [0.1],
        "epsilon_range": [0.1, 4.0],
        "delta": 0.01
    },
    {
        "name": "query2AllegationsNeighborhood",
        "csv_path": "DatasetForPrivacy/bpd-allegations.csv",
        "meta_path": "DatasetForPrivacy/bpd-allegations.yaml",
        "query": """
            SELECT neighborhood, COUNT(*) AS frequency
            FROM bpd_allegations.bpd_allegations
            WHERE neighborhood IS NOT NULL
            GROUP BY neighborhood
            ORDER BY frequency DESC;
        """,
        # "epsilon_range": [0.1],
         "epsilon_range": [0.1, 4.0],
        "delta": 0.01
    },
    {
        "name": "query4OfficersSalaries",
        "csv_path": "DatasetForPrivacy/officers_employees.csv",
        "meta_path": "DatasetForPrivacy/officers_employees.csv",
        "query": """
            SELECT title, AVG(total) AS avgSalaries
            FROM officers
            WHERE title IS NOT NULL
            GROUP BY title
            HAVING AVG(total) IS NOT NULL
            ORDER BY avgSalaries DESC;
        """,
        # "epsilon_range": [0.1],
         "epsilon_range": [0.1, 4.0],
        "delta": 0.01
    },
    {
        "name": "query5ShootingsNeighborhood",
        "csv_path": "DatasetForPrivacy/bpd-allegations.csv",
        "meta_path": "DatasetForPrivacy/bpd-allegations.yaml",
        "query": """
            SELECT neighborhood, COUNT(*) AS totalVictims
            FROM shootings
            WHERE neighborhood IS NOT NULL
            GROUP BY neighborhood
            ORDER BY totalVictims DESC;
        """,
        # "epsilon_range": [0.1],
         "epsilon_range": [0.1, 4.0],
        "delta": 0.01
    }
    # Add more query objects as needed
]
