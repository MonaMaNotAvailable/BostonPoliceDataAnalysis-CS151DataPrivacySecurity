queries = [
    {
        "name": "query3AllegationCountOnOfficers",
        "csv_path": "DatasetForPrivacy/AllegationCountOnOfficers.csv",
        "meta_path": "DatasetForPrivacy/AllegationCountOnOfficers.yaml",
        "query": """
            SELECT
                first_name,
                last_name,
                ranking,
                COUNT(allegation)/2 AS allegation_count
            FROM
                AllegationCountOnOfficers.AllegationCountOnOfficers
            WHERE
                active = TRUE
            GROUP BY
                first_name,
                last_name,
                ranking
            ORDER BY allegation_count DESC
        """,
        "epsilon_range": [2.02],
        "delta": 0.01,
        "aggregrated_column": 2
    },
    # {
    #     "name": "query3AllegationCountOnOfficersWithRank",
    #     "csv_path": "DatasetForPrivacy/AllegationCountOnOfficers.csv",
    #     "meta_path": "DatasetForPrivacy/AllegationCountOnOfficers.yaml",
    #     "query": """
    #         SELECT
    #             first_name,
    #             last_name,
    #             ranking,
    #             COUNT(allegation)/2 AS allegation_count
    #         FROM
    #             AllegationCountOnOfficers.AllegationCountOnOfficers
    #         WHERE
    #             active = TRUE and ranking = 'ptl'
    #         GROUP BY
    #             first_name,
    #             last_name,
    #             ranking
    #         ORDER BY allegation_count DESC
    #     """,
    #     "epsilon_range": [2.02],
    #     "delta": 0.01,
    #     "aggregrated_column": 2
    # }
]