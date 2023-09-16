import math
class ListV2: 
    
    def __init__(self,values):
       
        self.value=0
        self.values=list(values)
        
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.values)>self.value:
            result=self.values[self.value]
            self.value = self.value + 1
            return result 
        else:
            raise StopIteration
    
    def __add__(self, other):
        return ListV2([a + b for a, b in zip(self.values, other.values)])
        
    def mean(self):
        return sum(self.values)/len(self.values)
    
    def append(self,other):
        if type(other) in (str,float,int):
            return self.values.append(other)
        
    def __repr__(self):
        return str(self.values)

class DataFrame:
    def __init__(self, data, columns):
            current_index=0
            self.columns=list(columns)
                    
            self.index={}

            self.data_dict={'': ListV2([])}
            for col in columns:
                self.data_dict.update({col:ListV2([])})

            for row_index, row_data in enumerate(data):
                    self.data_dict[''].append(current_index)
                    self.index[self.data_dict[''].values[row_index]] = current_index
                    for col_index, cell_value in enumerate(row_data):
                        self.data_dict[columns[col_index]].append(cell_value)
                        
                    current_index+=1
 

    def __getitem__(self, value):


        if type(value) in [str, int, float]:
            return self.data_dict[value]
        
        elif isinstance(value, slice):
            start = value.start or 0
            stop = value.stop or len(self.index)
            step = value.step or 1
            columns = list(self.data_dict.keys())[1:]
            data = [list(self.data_dict[col].values[start:stop:step]) for col in columns]
            return DataFrame(list(zip(*data)), columns=columns)

        elif type(value) in [list]:
            temp = []
            i = 0
            while i < len(self.index):
                temp2 = []
                for j in value:
                    temp2.append(self.data_dict[j].values[i])
                temp.append(temp2)
                i += 1
            return DataFrame(temp, value)

        elif isinstance(value, tuple):
            temp = []
            columns = []
            for i in range(value[1].start or 0, value[1].stop or len(self.index), value[1].step or 1):
                columns.append(list(self.data_dict.keys())[i+1])
            for i in range(value[0].start or 0, value[0].stop or len(self.index), value[0].step or 1):
                temp2 = []
                for j in columns:
                    temp2.append(self.data_dict[j].values[i])
                temp.append(temp2)
            return DataFrame(temp, columns=columns)


    def as_type(self, value, new_type):
        temp = []
        for x in self.data_dict[value]:
            temp.append(new_type(x))
        self.data_dict[value].values = temp
        return self.data_dict[value]
    

    def mean(self):
        temp = {}
        for key, value in self.data_dict.items():
            if key in ['']:
                pass
            else:
                temp[key] = (sum(value.values)/len(value.values))
        return temp  
    
    def drop(self, key):
        del self.data_dict[key]
        columns_list = list(self.columns)
        columns_list.remove(key)
        self.columns = list(columns_list)

    def set_index(self, column):
            self.data_dict[''] = ListV2(column)


    def loc(self, loc_logic):
        list1 = []
        if isinstance(loc_logic, int):
            list1 = [self.data_dict[col].values[loc_logic] for col in self.columns]
        else:
            row_id = []
            for row in loc_logic[0]:
                row_id.append(self.data_dict[''].values.index(row))
                
            df_cols = loc_logic[1]
            list1 = []
            row_idx = 0
            while row_idx < len(row_id):
                rows_location = []
                col_idx = 0
                while col_idx < len(df_cols):
                    rows_location.append(self.data_dict[df_cols[col_idx]].values[row_id[row_idx]])
                    col_idx += 1
                list1.append(rows_location)
                row_idx += 1

            temp = DataFrame(list1, df_cols)
            temp.set_index(loc_logic[0])
            index_dict = temp.index
            loc_temp = len(list(index_dict.keys()))
            loc_dict = {}

            i = 0
            while i < loc_temp:
                loc_dict[loc_logic[0][i]] = index_dict[i]
                i += 1
            temp.index = loc_dict
            return temp


    def iterrows(self):
        index = 0
        temp = []
        
        while index < len(self.data_dict[self.columns[0]].values):

            temp2 = []
            for col in self.columns:
                    column_data = self.data_dict.get(col)
                    if column_data is not None:
                        value = column_data.values[index]
                        temp2.append(value)
            keys = self.data_dict[''].values[index]
                           
            temp2 = tuple(temp2)
            temp.append((keys, temp2))
            index += 1

        return temp
            
    def iteritems(self):
        temp = {}
                      
        for i in self.columns: 
            # Loop over the column and add  values to the dict
            temp[i]=self.data_dict[i].values
        return temp # Return the dictionary of column nams and values.

    def __repr__(self):
        header = ','.join(self.data_dict.keys())
        rows_data = []

        for i in range(len(self.index)):
                row = [str(self.data_dict[j].values[i]) for j in self.data_dict]
                
                rows_data.append(','.join(row))

                final_repr = '\n'.join([header] + rows_data )

        return final_repr
    
    