"""
    A small class to easily create and execute queries after given the table to query,
alongside the joins (if any) and filters (if any) for the query.
"""

class Query_Interface():
    """
    :param tbl: models.py Table.
    :param joins: Python list of [<table name>,...].
    :param filters: Python dict of {<field>: <value>/[<value1>,...]}
    :param first: Boolean for either first record or all records.
    """

    Main_table = None
    Join = []
    Filters = {}
    First = True
    Q = None
    Join_types = {
        'User': {'Direct': ['documents'], 'Secondary': []},
        'Documents': {'Direct': ['uid'], 'Secondary': []}
    }

    def __init__(self, tbl, joins=[], filters={}, first=True):
        self.Main_table = tbl
        self.First = first
        if type(joins) is list:
            self.Join = joins
        elif type(joins) is str:
            self.Join = [joins]
        else:
            raise TypeError("`joins` parameter accepts list of str or str")
        if type(filters) is not dict:
            raise TypeError("`filters` parameter accepts dict `{<filter>: <value>}` or `{<filter>: [<value1>,...]`")
        else:
            self.Filters = filters

    def __repr__(self):
        return "<Database Query Interface>"

    def print_attr(self):
        if self.First:
            out = "Acquiring first result of "
        else:
            out = "Acquiring all results of "
        out += "Table `{}` ".format(self.Main_table)
        if len(self.Join) > 0:
            out += "joined with: "
            for j in self.Join:
                out += "`{}`, ".format(j)

        if len(self.Filters) > 0:
            out += "filtering with: "
            for f in self.Filters:
                out += "`{}` as `{}`, ".format(f, self.Filters[f])
        out = out[:-2]
        print(out)

    def Fetch(self):
        self.Q = self.Main_table.query
        if len(self.Join) > 0:
            self.Q = self._joins(self.Q, self.Main_table)
        if len(self.Filters) > 0:
            self.Q = self._filters(self.Q, self.Main_table)
        if self.First:
            return self.Q.first()
        else:
            return self.Q.all()

    def _joins(self, query, Table):  # TODO: Add some join code...
        joins = self.Join_types.get(Table, None)
        for j in self.Join:
            if j in joins['Direct']:
                query = query.join( getattr( Table, j ) )  # TODO: Thank you, come again!
            elif j in joins['Secondary']:
                print("Secondary not implemented!")  # TODO: Any secondary joins?
                # Join on the tables own attribute which is the association between tables.
                pass
        return query

    def _filters(self, query, Table):  # TODO: Add some filters code...
        for f in self.Filters:
            # Something for type
            # string matches / string contains filter
            # numerical match / gt/lt/gte/lte/eq
            # bool
            # datetime ranging
            pass
        return query

# End class #
