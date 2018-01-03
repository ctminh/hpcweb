# -*- coding: utf-8 -*-

from odoo import models, fields, api

class hpcuser(models.Model):
    _name = 'hpcuser.user'

    name = fields.Char('User Name')
    status = fields.Text('Status')
    job = fields.One2many('hpcuser.job', 'user_id', 'Job')


class queue(models.Model):
    _name = 'hpcuser.queue'

    name = fields.Char('Queue Name')
    node = fields.Char('Node')
    job = fields.One2many('hpcuser.job', 'queue_id', 'Job')


class job(models.Model):
    _name = 'hpcuser.job'

    name = fields.Char('Job Name')
    status = fields.Text('Status')
    queue_time = fields.Datetime('Queue Time')
    wall_time = fields.Datetime('Wall Time')

    user_id = fields.Many2one('hpcuser.user', 'User', ondelete='cascade')
    queue_id = fields.Many2one('hpcuser.queue', 'Queue', ondelete='cascade')

    start_time = fields.Datetime('Start Time')
    end_time = fields.Datetime('End Time')

    r_cpu = fields.Float('Required CPU')
    r_mem = fields.Float('Required Mem')
    r_disk = fields.Float('Required Disk')

    a_cpu = fields.Float('Average CPU')
    a_mem = fields.Float('Average Mem')
    a_disk = fields.Float('Average Disk')


