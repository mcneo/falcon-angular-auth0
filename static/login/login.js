angular.module('base')
    .controller('LoginCtrl', function ($scope, auth, $rootScope) {
        $scope.auth = auth;
    });
