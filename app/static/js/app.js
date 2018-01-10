'use strict';   // See note about 'use strict'; below


angular.module('myApp', [
    'ngRoute'
])


    .config(['$routeProvider',
        function ($routeProvider) {
            $routeProvider.when('/', {
                controller: 'CountryListController',
                templateUrl: '/static/partials/index.html'
            }).when('/about', {
                templateUrl: '../static/partials/about.html'
            }).otherwise({
                redirectTo: '/'
            });
            //$locationProvider.html5Mode(true);
            //$locationProvider.hashPrefix('');
        }])


    .controller('CountryListController', function ($scope, $http) {

        $http({
            method: 'GET',
            url: '/api/countries'
        }).then(function (response) {
                $scope.countries = response.data.countries; // response data
            });

        $scope.show = function (country) {
            $http({
                method: 'GET',
                url: '/api/countries/' + country
            }).then(function (response) {
                $scope.wahlkreise = response.data.wahlkreise
            })
        }
    });
