{
 "name": "Reclamacions",
 "version": "1.0",
 "application": True,
 "depends": ["base", "sale"],
 "data": [
    'security/ir.model.access.csv',
    'views/complaint_views.xml',
    'views/complaint_reason_views.xml',
 ],
 "installable": True,
 "license": "LGPL-3",
}