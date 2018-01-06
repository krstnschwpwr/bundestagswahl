'use strict';

function CountryListController($scope, $http) {
     $http({method: 'GET', url: 'http://0.0.0.0:5050/api/countries'}).success(function(data) {
      $scope.countries = data.deals; // response data
    });
}