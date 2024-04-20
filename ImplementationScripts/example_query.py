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
        "epsilon_range": [0.01, 0.1, 0.5, 1.0, 1.6666666666666665, 2.333333333333333, 3.0, 3.6666666666666665, 4.333333333333333, 5.0],
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
        "epsilon_range": [0.1, 0.5333333333333333, 0.9666666666666667, 1.4000000000000001, 1.8333333333333335, 2.266666666666667, 2.7, 3.1333333333333333, 3.566666666666667, 4.0],
        "delta": 0.01
    },
    {
        "name": "query3AllegationCountOnOfficers",
        "csv_path": "DatasetForPrivacy/AllegationCountOnOfficers.csv",
        "meta_path": "DatasetForPrivacy/AllegationCountOnOfficers.yaml",
        "query": """
            SELECT
                first_name,
                last_name,
                COUNT(allegation)/2 AS allegation_count
            FROM
                AllegationCountOnOfficers.AllegationCountOnOfficers
            WHERE
                active = TRUE
            GROUP BY
                first_name,
                last_name
            ORDER BY allegation_count DESC
        """,
        "epsilon_range": [0.05, 0.37777777777777777, 0.7055555555555556, 1.0333333333333334, 1.3611111111111112, 1.6888888888888889, 2.0166666666666666, 2.344444444444444, 2.672222222222222, 3.0],
        "delta": 0.01,
        "aggregrated_column": 2
    },
    {
        "name": "query4OfficersSalaries",
        "csv_path": "DatasetForPrivacy/officers_employees.csv",
        "meta_path": "DatasetForPrivacy/officers_employees.yaml",
        "query": """
            SELECT title, AVG(total) AS avgSalaries
            FROM officers_employees.officers_employees
            WHERE title IS NOT NULL
            GROUP BY title
            HAVING AVG(total) > 0
            ORDER BY avgSalaries DESC;
        """,
         "epsilon_range": [9.0, 14.666666666666668, 20.333333333333336, 26.0, 31.666666666666668, 37.333333333333336, 43.0, 48.66666666666667, 54.333333333333336, 60.0],
        "delta": 0.01
    },
    {
        "name": "query5ShootingsNeighborhood",
        "csv_path": "DatasetForPrivacy/PersonShot.csv",
        "meta_path": "DatasetForPrivacy/PersonShot.yaml",
        "query": """
            SELECT NEIGHBORHOOD, COUNT(*) AS totalVictims
            FROM PersonShot.PersonShot
            WHERE NEIGHBORHOOD IS NOT NULL
            GROUP BY NEIGHBORHOOD
            ORDER BY totalVictims DESC;
        """,
         "epsilon_range": [1.0, 1.1444444444444444, 1.2888888888888888, 1.4333333333333333, 1.5777777777777777, 1.722222222222222, 1.8666666666666667, 2.011111111111111, 2.1555555555555554, 2.3],
        "delta": 0.01
    }
]