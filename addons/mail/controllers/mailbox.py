# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.http import request


class MailboxController(http.Controller):
    @http.route("/mail/inbox/messages", methods=["POST"], type="json", auth="user")
    def discuss_inbox_messages(self, search_term=None, before=None, after=None, limit=30, around=None):
        domain = [("needaction", "=", True)]
        res = request.env["mail.message"]._message_fetch(domain, search_term=search_term, before=before, after=after, around=around, limit=limit)
        messages = res.pop("messages")
        return {
            **res,
            "messages": messages._message_format(for_current_user=True, add_followers=True),
        }

    @http.route("/mail/history/messages", methods=["POST"], type="json", auth="user")
    def discuss_history_messages(self, search_term=None, before=None, after=None, limit=30, around=None):
        domain = [("needaction", "=", False)]
        res = request.env["mail.message"]._message_fetch(domain, search_term=search_term, before=before, after=after, around=around, limit=limit)
        return {**res, "messages": res["messages"]._message_format(for_current_user=True)}

    @http.route("/mail/starred/messages", methods=["POST"], type="json", auth="user")
    def discuss_starred_messages(self, search_term=None, before=None, after=None, limit=30, around=None):
        domain = [("starred_partner_ids", "in", [request.env.user.partner_id.id])]
        res = request.env["mail.message"]._message_fetch(domain, search_term=search_term, before=before, after=after, around=around, limit=limit)
        return {**res, "messages": res["messages"]._message_format(for_current_user=True)}
