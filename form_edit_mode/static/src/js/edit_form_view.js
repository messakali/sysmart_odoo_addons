openerp.form_edit_mode = function (instance) {

    instance.web.FormView.include({

        init: function(parent, dataset, view_id, options) {  
        	if (options.action != null && options.action.target != null && options.action.target == 'current_edit') { 
        		options.initial_mode = "edit";	
        	}
        	
            this._super(parent, dataset, view_id, options);
        },
        });  

};
