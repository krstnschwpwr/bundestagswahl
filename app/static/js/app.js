'use strict';   // See note about 'use strict'; below


angular.module('myApp', [
    'ngRoute', 'chart.js'
])


    .config(['$routeProvider', '$locationProvider',
        function ($routeProvider, $locationProvider) {
            $routeProvider.when('/', {
                templateUrl: '/static/partials/index.html'
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
                var chartLabels = [];
                var chartData = [];
                response.data.forEach(function (d) {
                        chartLabels.push(d[0]);
                        chartData.push(d[1])
                });
                $scope.labels = chartLabels;
                $scope.data = chartData;

            })
        };
        $('.kreis ').click(function () {
            $('.btnred').fadeIn(1000).css('display', 'block');
        });
        $('.button ').click(function () {
            $('#results').fadeIn(1000).css('display', 'block');
        });

        $scope.select = function (index) {
            $scope.selected2 = false;
            $scope.selected = true;
            $scope.selected = index;
        };
        $scope.sel = function (index) {
            $scope.selected2 = true;
            $scope.selected2 = index;
        };


    });

