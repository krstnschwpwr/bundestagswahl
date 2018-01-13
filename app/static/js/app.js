'use strict';   // See note about 'use strict'; below


angular.module('myApp', [
    'ngRoute', 'chart.js'
])


    .config(['$routeProvider', '$locationProvider',
        function ($routeProvider, $locationProvider) {
            $routeProvider.when('/', {
                templateUrl: '/static/partials/index.html'
            }).when('/about', {
                templateUrl: '../static/partials/about.html'
            }).otherwise({
                redirectTo: '/'
            });
            $locationProvider.html5Mode(true).hashPrefix('*');
        }])


    .controller('CountryListController', function ($scope, $http) {

        $http({
            method: 'GET',
            url: '/api/countries'
        }).then(function (response) {
            $scope.countries = response.data.countries; // response data
        });

        $scope.show = function (bundeslandId) {
            $scope.details = null;
            $scope.labels = null;
            $scope.data = null;
            $http({
                method: 'GET',
                url: '/api/countries/' + bundeslandId
            }).then(function (response) {
                $scope.wahlkreise = response.data.wahlkreise;
            })
        };

        $scope.showDetails = function (wahlkreis_id) {
            $http({
                method: 'GET',
                url: '/api/countries/detail/' + wahlkreis_id
            }).then(function (response) {
                $scope.details = response.data;
                $scope.labels = Object.keys(response.data);
                $scope.data = Object.values(response.data);
            })
        };


    });
