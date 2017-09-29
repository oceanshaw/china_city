# _*_ coding: utf-8 _*_
{
    'name': "中国地区导入",
    'version': '1.0',
    'depends': ["base"],
    'author': "Ocean",
    'website': "www.ifeige.cn",
    'category': 'Other',
    'description': """
    中国地区导入
    """,

    'data': [
        'security/ir.model.access.csv',
        'views/city.xml',
        'views/partner.xml',
        'views/region.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'installable':True,
}
