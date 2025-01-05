/** @odoo-module */

import { useService } from '@web/core/utils/hooks';
import { getCurrency } from '@web/core/currency';
import { Component, onWillStart, useState } from "@odoo/owl";

export class ExpenseDashboard extends Component {
    static template = "hr_expense.ExpenseDashboard";
    static props = {};

    setup() {
        super.setup();
        this.orm = useService('orm');
        this.actionService = useService("action");

        this.state = useState({
            expenses: {}
        });

        onWillStart(async () => {
            const expense_states = await this.orm.call("hr.expense", 'get_expense_dashboard', []);
            this.state.expenses = expense_states;
        });
    }

    renderMonetaryField(value, currency_id) {
        value = value.toFixed(2);
        const currency = getCurrency(currency_id);
        if (currency) {
            if (currency.position === "after") {
                value += currency.symbol;
            } else {
                value = currency.symbol + value;
            }
        }
        return value;
    }

    async applyFilter(filterName) {
        const { actionId } = this.env.config;
        const action = actionId ? await this.actionService.loadAction(actionId) : {};

        action['context'] = { [`search_default_${filterName}`]: 1 };
        action['tag'] = 'menu'; //disables breadcrumb change on filter change
        return this.actionService.doAction(action);
    }
}
