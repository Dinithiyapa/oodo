/** @odoo-module **/

    import { _t } from "@web/core/l10n/translation";
    import wTourUtils from "@website/js/tours/tour_utils";

    import { markup } from "@odoo/owl";

    wTourUtils.registerWebsitePreviewTour("website_event_tour", {
        test: true,
        url: "/",
    }, () => [{
        content: _t("Click here to add new content to your website."),
        trigger: ".o_menu_systray .o_new_content_container > a",
        consumeVisibleOnly: true,
        position: 'bottom',
        run: "click",
    }, {
        trigger: "a[data-module-xml-id='base.module_website_event']",
        content: _t("Click here to create a new event."),
        position: "bottom",
        run: "click",
    }, {
        trigger: '.modal-dialog div[name="name"] input',
        content: markup(_t("Create a name for your new event and click <em>\"Continue\"</em>. e.g: Technical Training")),
        run: "edit Technical Training",
        position: "left",
    }, {
        trigger: '.modal-dialog div[name=date_begin]',
        content: _t("Open date range picker. Pick a Start date for your event"),
        run: function () {
            const el1 = document.querySelector('input[data-field="date_begin"]');
            el1.value = '09/30/2020 08:00:00';
            el1.dispatchEvent(new Event("change", { bubbles: true, cancelable: true }));
            const el2 = document.querySelector('input[data-field="date_end"]');
            el2.value = '10/02/2020 23:00:00';
            el2.dispatchEvent(new Event("change", { bubbles: true, cancelable: true }));
            el1.click();
        }
    }, {
        trigger: '.modal-footer button.btn-primary',
        extra_trigger: `.modal-dialog input[type=text]:not(:value(""))`,
        content: markup(_t("Click <em>Continue</em> to create the event.")),
        position: "right",
        run: "click",
    }, {
        trigger: "#oe_snippets.o_loaded #snippet_structure .oe_snippet:eq(2) .oe_snippet_thumbnail",
        content: _t("Drag this block and drop it in your page."),
        position: "bottom",
        run: `drag_and_drop(:iframe #wrapwrap > main)`,
    }, {
        trigger: "button[data-action=save]",
        content: _t("Once you click on save, your event is updated."),
        position: "bottom",
        // Wait until the drag and drop is resolved (causing a history step)
        // before clicking save.
        extra_trigger: ".o_we_external_history_buttons button.fa-undo:not([disabled])",
        run: "click",
    }, {
        trigger: ".o_menu_systray_item.o_website_publish_container a",
        extra_trigger: ":iframe body:not(.editor_enable)",
        content: _t("Click to publish your event."),
        position: "top",
        run: "click",
    }, {
        trigger: ".o_website_edit_in_backend > a",
        content: _t("Click here to customize your event further."),
        position: "bottom",
        isCheck: true,
    }]);
