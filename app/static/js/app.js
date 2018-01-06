'use strict';   // See note about 'use strict'; below

var myApp = angular.module('myApp', ['ngRoute']);


myApp.config(['$routeProvider',
     function($routeProvider) {
         $routeProvider.
             when('/home', {
                 templateUrl: '/static/partials/index.html',
                controller: CountryListController
             }).
             otherwise({
                 redirectTo: '/'
             });
         $locationProvider.html5Mode(true);
		$locationProvider.hashPrefix('');
    }]);