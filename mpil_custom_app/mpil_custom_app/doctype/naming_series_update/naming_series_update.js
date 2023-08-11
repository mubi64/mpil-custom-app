// Copyright (c) 2023, Sowaan and contributors
// For license information, please see license.txt

frappe.ui.form.on("Naming Series Update", {
  // refresh: function(frm) {

  // }
  execute: function (frm) {
    if (frm.doc.series) {
      console.log(frm.doc, typeof frm.doc);
      frappe.call({
        method:
          "mpil_custom_app.mpil_custom_app.doctype.naming_series_update.naming_series_update.execute_query",
        args: {
          doc: frm.doc,
        },
        callback: function (r) {
          if (!r.exc) {
            frm.set_value('current_value', r.message);
          }
        },
        freeze: true,
        freeze_message: __("Executing..."),
      });
    }
  },
});
