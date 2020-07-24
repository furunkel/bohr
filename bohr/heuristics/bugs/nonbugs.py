from bohr.heuristics.templates import bug_bugless__for_commit_message, fix_bugless__for_commit_message, \
    regex_version__for_commit_message, keyword_lookup_template, COMMIT_MESSAGE, ISSUE_CONTENTS, ISSUE_LABELS
from bohr.snorkel_utils import BUGLESS

heuristics = [bug_bugless__for_commit_message, fix_bugless__for_commit_message, regex_version__for_commit_message] \
+ keyword_lookup_template(label=BUGLESS, terms=[
    'ad',
    'add',
    'addit',
    'cleanup',
    'deprec',
    'document',
    'enhanc',
    'exclud',
    'implement',
    'improv',
    'new',
    'note',
    'optim',
    'perform',
    'plugin',
    'provid',
    'publish',
    'readm',
    'refactor',
    'restructur',
    'todo',
    'updat',
 ]) + keyword_lookup_template(label=BUGLESS, terms=[
    'abil',
    'allow',
    'analysi',
    'baselin',
    'benchmark',
    'better',
    'chang log',
    'consolid',
    'create',
    'develop',
    'doc',
    'extend'
    'gener',
    'gitignor',
    'includ',
    'intorduc',
    'javadoc',
    'move',
    'opinion',
    'optimis',
    'polish',
    'prepar',
    'set up',
    'simplif',
    'simplifi',
    'statist',
    'support',
    'test coverag',
    'tweak',
    'upgrad',
], restrict_to_fields=[COMMIT_MESSAGE, ISSUE_CONTENTS])  + keyword_lookup_template(label=BUGLESS, terms=[
    'bump',
    'idea',
    'modif',
    'possibl',
    'propos',
    'reduc',
    'refin',
    'reimplement',
    'renam',
    'reorgan',
    'replac',
    'review',
    'rewrit',
    'rid',
    'speed up',
    'speedup',
    'unit',
], restrict_to_fields=[ISSUE_CONTENTS, ISSUE_LABELS]) + keyword_lookup_template(label=BUGLESS, terms=[
    'build',
    'chang',
    'check',
    'do not',
    'dont',
    'junit',
    'miss',
], restrict_to_fields=[ISSUE_LABELS])  + keyword_lookup_template(label=BUGLESS, terms=[
    'beautification',
    'clean',
    'comment',
    'configur chang',
    'log',
    'minim',
    'pass test',
    'perf test',
    'perfom test',
    'reformat',
    'release',
    'stage',
    'stat',
    'switch',
    'test pass',
    'version',
], restrict_to_fields=[COMMIT_MESSAGE]) + keyword_lookup_template(label=BUGLESS, terms=[
    'avoid',
    'convert',
    'drop',
    'expand',
    'forget',
    'format',
    'limit',
    'remov',
    'restrict',
    'unnecessari',
    'use',
    'regress test',
], restrict_to_fields=[ISSUE_CONTENTS])  + keyword_lookup_template(label=BUGLESS, terms=[
    'complet',
    'exampl',
    'info',
    'migrat',
], restrict_to_fields=[COMMIT_MESSAGE, ISSUE_LABELS]) + keyword_lookup_template(label=BUGLESS, terms=[
    'featur',
], only_full_word=False)