"""This file contains dictionaries that have DOIs as keys and the doi_provider as the values. It is used by the migrator_recursion.py"""

# award_doi_prov are award doi
award_doi_prov = [{'id': 'gold:Gs0114675', 'doi': 'doi:10.46936/jejc.proj.2014.48483/60005501', 'doi_prov': 'emsl'},
                  {'id': 'gold:Gs0110138',
                      'doi': 'doi:10.46936/sthm.proj.2016.49279/60005943', 'doi_prov': 'emsl'},
                  {'id': 'gold:Gs0114663',
                      'doi': 'doi:10.46936/jejc.proj.2014.48473/60005497', 'doi_prov': 'emsl'},
                  {'id': 'gold:Gs0128850',
                      'doi': 'doi:10.46936/sthm.proj.2017.49804/60006181', 'doi_prov': 'emsl'},
                  {'id': 'nmdc:sty-11-t91cwb40',
                      'doi': 'doi:10.46936/10.25585/60001061', 'doi_prov': 'jgi'},
                  {'id': 'nmdc:sty-11-5bgrvr62',
                      'doi': 'doi:10.46936/10.25585/60001198', 'doi_prov': 'jgi'},
                  {'id': 'nmdc:sty-11-5tgfr349',
                      'doi': 'doi:10.46936/10.25585/60001289', 'doi_prov': 'jgi'},
                  {'id': 'nmdc:sty-11-5tgfr349',
                      'doi': 'doi:10.46936/sarr.proj.2018.50298/60000034', 'doi_prov': 'emsl'},
                  {'id': 'nmdc:sty-11-5tgfr349',
                      'doi': 'doi:10.46936/cpcy.proj.2019.51180/60006718', 'doi_prov': 'emsl'},
                  {'id': 'gold:Gs0135149',
                      'doi': 'doi:10.46936/fics.proj.2017.49991/60006232', 'doi_prov': 'emsl'},
                  {'id': 'gold:Gs0110119',
                      'doi': 'doi:10.46936/10.25585/60000762', 'doi_prov': 'jgi'},
                  {'id': 'nmdc:sty-11-r2h77870',
                      'doi': 'doi:10.46936/10.25585/60000017', 'doi_prov': 'jgi'},
                  {'id': 'nmdc:sty-11-28tm5d36',
                      'doi': 'doi:10.46936/intm.proj.2021.60141/60000423', 'doi_prov': 'emsl'},
                  {'id': 'nmdc:sty-11-db67n062',
                      'doi': 'doi:10.46936/sarr.proj.2018.50267/60000030', 'doi_prov': 'emsl'},
                  {'id': 'nmdc:sty-11-8xdqsn54', 'doi': 'doi:10.46936/lser.proj.2019.50718/60006575', 'doi_prov': 'emsl'}]

# new_award_dois are new award dois that need to be added to mongo
new_award_dois = [{'id': 'gold:Gs0110138', 'doi': 'doi:10.46936/10.25585/60001027', 'doi_prov': 'jgi'},
                  {'id': 'gold:Gs0128850',
                      'doi': 'doi:10.46936/10.25585/60000880', 'doi_prov': 'jgi'},
                  {'id': 'gold:Gs0103573', 'doi': 'doi:10.46936/10.25585/60000910', 'doi_prov': 'jgi'}]

# award_move_to_data are dois that are currently listed as award_dois, but need to be moved to dataset_dois
award_move_to_data = [{'id': 'gold:Gs0114675', 'doi': 'doi:10.25585/1487763', 'doi_prov': 'jgi'},
                      {'id': 'gold:Gs0110138',
                          'doi': 'doi:10.25585/1488099', 'doi_prov': 'jgi'},
                      {'id': 'gold:Gs0114663',
                          'doi': 'doi:10.25585/1487765', 'doi_prov': 'jgi'},
                      {'id': 'gold:Gs0128850',
                          'doi': 'doi:10.25585/1488160', 'doi_prov': 'jgi'},
                      {'id': 'gold:Gs0135149',
                          'doi': 'doi:10.25585/1488224', 'doi_prov': 'jgi'},
                      {'id': 'gold:Gs0103573', 'doi': 'doi:10.25585/1488096', 'doi_prov': 'jgi'}]
