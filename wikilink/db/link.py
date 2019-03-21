#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Provide Link - the main calss to initialize link table"""

# Third party modules
from sqlalchemy import Column, Integer, String, DateTime, text, ForeignKey

# own modules
from .base import Base

__author__ = "Tran Ly Vu (vutransingapore@gmail.com)"
__copyright__ = "Copyright (c) 2016 - 2019 Tran Ly Vu. All Rights Reserved."
__credits__ = ["Tranlyvu"]
__license__ = "Apache License 2.0"
__version__ = "1.2.0"
__maintainer__ = "Tran Ly Vu"
__email__ = "vutransingapore@gmail.com"
__status__ = "Production"

class Link(Base):
	"""Link table"""
	__tablename__ = 'link'

	id = Column(Integer, primary_key=True)
	from_page_id = Column(Integer, ForeignKey('page.id'))
	to_page_id = Column(Integer, ForeignKey('page.id'))
	number_of_separation = Column(Integer, nullable=False)
	created = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))

	def __repr__(self):
		return "<Link(from_page_id='%s', to_page_id='%s', number_of_separation='%s', created='%s')>" % (
			self.from_page_id, self.to_page_id, self.number_of_separation, self.created)
