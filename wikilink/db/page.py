#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Provide Page - the main calss to initialize page table"""

# third party modules
from sqlalchemy import Column, Integer, String, DateTime, text, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT

# own modules
from .base import Base

__author__ = "Tran Ly Vu (vutransingapore@gmail.com)"
__copyright__ = "Copyright (c) 2016 - 2019 Tran Ly Vu. All Rights Reserved."
__credits__ = ["Tranlyvu"]
__license__ = "Apache License 2.0"
__maintainer__ = "Tran Ly Vu"
__email__ = "vutransingapore@gmail.com"
__status__ = "Production"


class Page(Base):
	"""Page table"""

	__tablename__ = 'page'

	id = Column(Integer(), primary_key=True)
	url = Column(LONGTEXT)
	created = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))

	def __repr__(self):
		return "<Page(page_id = '%s', url ='%s', created='%s')>" % (self.page_id, self.url, self.created)