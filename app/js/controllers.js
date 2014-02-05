'use strict';

/* Controllers */

var phonecatApp = angular.module('phonecatApp', []);

phonecatApp.controller('PhoneListCtrl', function($scope, $http) {
    $scope.jeff = { age: 'Loading..',
		    name: 'Loading..'
    };
    $http({method: "GET", url: 'http://localhost:8001'}).success(function(data) {
	$scope.jeff = data;
    });
});
