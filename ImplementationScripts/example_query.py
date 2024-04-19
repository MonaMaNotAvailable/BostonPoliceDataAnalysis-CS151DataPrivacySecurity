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
        "epsilon_range": [50.0, 83.33333333333334, 116.66666666666667, 150.0, 183.33333333333334, 216.66666666666669, 250.0, 283.33333333333337, 316.6666666666667, 350.0],
        "delta": 10
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
        "epsilon_range": [15.0, 33.33333333333333, 51.666666666666664, 70.0, 88.33333333333333, 106.66666666666666, 125.0, 143.33333333333331, 161.66666666666666, 180.0],
        "delta": 10
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
        "epsilon_range": [10.0, 14.444444444444445, 18.88888888888889, 23.333333333333336, 27.77777777777778, 32.22222222222222, 36.66666666666667, 41.111111111111114, 45.55555555555556, 50.0],
        "delta": 10,
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
         "epsilon_range": [500.0, 611.1111111111111, 722.2222222222222, 833.3333333333334, 944.4444444444445, 1055.5555555555557, 1166.6666666666667, 1277.7777777777778, 1388.888888888889, 1500.0],
        "delta": 10
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
         "epsilon_range": [100.0, 144.44444444444446, 188.88888888888889, 233.33333333333331, 277.77777777777777, 322.22222222222223, 366.66666666666663, 411.1111111111111, 455.55555555555554, 500.0],
        "delta": 10
    }
]