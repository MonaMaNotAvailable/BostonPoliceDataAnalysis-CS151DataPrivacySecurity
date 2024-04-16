queries = [
    {
        "name": "query1",
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
        "name": "query2",
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
    }
    # Add more query objects as needed
]
