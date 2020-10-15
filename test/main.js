var gridOptions = {
  columnDefs: [
    { field: 'name'},
    { field: 'phone' , cellRenderer: (invNum) => 
    `<a href="https://netzary.com">${invNum.value}</a>`  },
    { field: 'source'  , cellRenderer: (invNum) => 
    `<a href="https://netzary.com/${invNum.value}">${invNum.value}</a>`  },
    { field: 'source_id' },
    { field: 'lead_id' },
    { field: 'stage' },
    { field: 'stage_id' }
  ], 
  defaultColDef: {
    flex: 1,
    minWidth: 100,
    sortable: true,
    filter: true,
  },
  autoGroupColumnDef: {
    minWidth: 200,
  },
  groupDefaultExpanded: 1,
};



// setup the grid after the page has finished loading
document.addEventListener('DOMContentLoaded', function () {
  var gridDiv = document.querySelector('#myGrid');
  new agGrid.Grid(gridDiv, gridOptions);

  agGrid
    .simpleHttpRequest({
      url:
        'https://wellness.bangalore2.com/dashboard/leads2_api/',
    })
    .then(function (data) {
      gridOptions.api.setRowData(data.slice(0, 10));
    });
});