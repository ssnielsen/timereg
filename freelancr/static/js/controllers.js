var freelancrApp = angular.module('freelancrApp', ['ui.bootstrap', 'ngCookies']);

freelancrApp.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  }
]);

freelancrApp.controller('AppController', function($scope, $http, $modal) {
  $scope.selectedCustomer = null;
  $scope.selectedCustomerProjects = null;

  // Load all customers for customer list
  $http.get('customer').success(function(data) {
    $scope.customers = data;
    $scope.selectCustomer($scope.customers[0]);
  });

  // Function called in ng-click tag on customer in customer list
  $scope.selectCustomer = function(customer) {
    $scope.selectedCustomer = customer;
    $scope.loadProjects();
  };

  // Load projects for a single customer
  $scope.loadProjects = function() {
    $http.get('customer/' + $scope.selectedCustomer.id + '/projects/').success(function(data) {
      $scope.selectedCustomerProjects = data;
      var sum = function(prev, cur) { return prev+cur.duration; };
      for (var i = 0; i < $scope.selectedCustomerProjects.length; i++) {
        var total = $scope.selectedCustomerProjects[i].activities.reduce(sum, 0);
        $scope.selectedCustomerProjects[i].totalHours = total;
      }
      $scope.selectedCustomer.totalHours = $scope.selectedCustomerProjects.reduce(function(prev, cur) { return prev+cur.totalHours; }, 0);
    });
  };

  // Load acitivities for a single project
  $scope.projectActivities = function(project) {
    $http.get('project/' + project.id + '/activities/').success(function(data) {
      return data;
    });
  };

  // Delete an activity
  $scope.deleteActivity = function(activity) {
    $http.delete('activity/' + activity.id + '/').success(function(data) {
      $scope.loadProjects();
    });
  };

  // Called when clicking edit on activity row
  $scope.editActivityModal = function(activity) {
    var editActivityModalInstance = $modal.open({
      templateUrl: 'editActivityModal.html',
      controller: 'EditController',
      resolve: { activity: function() { return activity; } }
    });

    // Callback when submitting edit activity modal
    editActivityModalInstance.result.then(function (activity) {
      $http.put('activity/' + activity.id + '/', activity).success(function (data) {
        $scope.loadProjects();
      });
    });
  };

  // Event for reloading projects - used after activities has been edited/added/deleted
  $scope.$on('reloadProjects', function (event, args) {
    $scope.loadProjects();
  });

  // Add project
  $scope.addProject = function() {
    var addProjectModalInstance = $modal.open({
      templateUrl: 'addProjectModal.html',
      controller: 'AddProjectController'
    });

    addProjectModalInstance.result.then(function (name) {
      var newProject = {
        customer: $scope.selectedCustomer.id,
        name: name
      };

      $http.post('project/', newProject).success(function(data) {
        $scope.loadProjects();
      });
    });
  };

  // Remove a project
  $scope.removeProject = function(project) {
    var removeProjectModalInstance = $modal.open({
      templateUrl: 'removeProjectModal.html',
      controller: 'RemoveProjectController'
    });

    removeProjectModalInstance.result.then(function () {
      $http.delete('project/' + project.id + '/').success(function(data) {
        $scope.loadProjects();
      });
    });
  };

});

// Controller for adding an activity (each row in table is a controller)
freelancrApp.controller('AddController', function($scope, $http) {
  $scope.format = "yyyy-MM-dd";

  // Adds activity - used in form
  $scope.addActivity = function(project) {
    var newActivity = {
      project: project.id,
      date: $scope.date.getFullYear() + '-' + ($scope.date.getMonth()+1) + '-' + $scope.date.getDate(),
      duration: $scope.duration,
      description: $scope.description,
      rate: $scope.rate,
      billed: $scope.billed,
      payed: $scope.payed
    };

    // Post to service
    $http.post('activity/', newActivity).success(function(data) {
      $scope.$emit('reloadProjects', {}); // Update activities
    });
  };

  $scope.openDatePicker = function($event) {
    $event.preventDefault();
    $event.stopPropagation();
    $scope.opened = true;
  };
});

// Controller for edit activity modal
freelancrApp.controller('EditController', function($scope, $modalInstance, activity) {
  $scope.date = activity.date;
  $scope.description = activity.description;
  $scope.rate = activity.rate;
  $scope.duration = activity.duration;
  $scope.billed = activity.billed;
  $scope.payed = activity.payed;

  $scope.editActivity = function() {
    activity.date = $scope.date;
    activity.description = $scope.description;
    activity.rate = $scope.rate;
    activity.duration = $scope.duration;
    activity.billed = $scope.billed;
    activity.payed = $scope.payed;
    $modalInstance.close(activity);
  };

  $scope.cancel = function() {
    $modalInstance.dismiss('cancel');
  };
});

// Controller for adding a project
freelancrApp.controller('AddProjectController', function($scope, $modalInstance) {
  $scope.addProject = function() {
    $modalInstance.close($scope.name);
  };

  $scope.cancel = function() {
    $modalInstance.dismiss('cancel');
  };
});

// Controller for removing a project
freelancrApp.controller('RemoveProjectController', function($scope, $modalInstance) {
  $scope.removeProject = function() {
    $modalInstance.close();
  };

  $scope.cancel = function() {
    $modalInstance.dismiss('cancel');
  };
});

// Filter handling boolean values
freelancrApp.filter('bool', function() {
  return function(value) {
    return value ? "Yes" : "No";
  };
});