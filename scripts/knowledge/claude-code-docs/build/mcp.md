Title: Connect Claude Code to tools via MCP - Claude Code Docs

URL Source: https://docs.anthropic.com/en/docs/claude-code/mcp

Markdown Content:
> ## Documentation Index
> 
> 
> Fetch the complete documentation index at: [https://code.claude.com/docs/llms.txt](https://code.claude.com/docs/llms.txt)
> 
> 
> Use this file to discover all available pages before exploring further.

Claude Code can connect to hundreds of external tools and data sources through the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction), an open source standard for AI-tool integrations. MCP servers give Claude Code access to your tools, databases, and APIs.Connect a server when you find yourself copying data into chat from another tool, like an issue tracker or a monitoring dashboard. Once connected, Claude can read and act on that system directly instead of working from what you paste.

## What you can do with MCP

With MCP servers connected, you can ask Claude Code to:

*   **Implement features from issue trackers**: “Add the feature described in JIRA issue ENG-4521 and create a PR on GitHub.”
*   **Analyze monitoring data**: “Check Sentry and Statsig to check the usage of the feature described in ENG-4521.”
*   **Query databases**: “Find emails of 10 random users who used feature ENG-4521, based on our PostgreSQL database.”
*   **Integrate designs**: “Update our standard email template based on the new Figma designs that were posted in Slack”
*   **Automate workflows**: “Create Gmail drafts inviting these 10 users to a feedback session about the new feature.”
*   **React to external events**: An MCP server can also act as a [channel](https://code.claude.com/docs/en/channels) that pushes messages into your session, so Claude reacts to Telegram messages, Discord chats, or webhook events while you’re away.

## Popular MCP servers

Here are some commonly used MCP servers you can connect to Claude Code:

Event platform for managing tickets, orders & more Command

`claude mcp add --transport http tickettailor https://mcp.tickettailor.ai/mcp`

Manage issues, projects & team workflows in Linear Command

`claude mcp add --transport http linear https://mcp.linear.app/mcp`

Access the Hugging Face Hub and thousands of Gradio Apps Command

`claude mcp add --transport http hugging-face https://huggingface.co/mcp`

Search, access, and get insights on your Amplitude data Command

`claude mcp add --transport http amplitude https://mcp.amplitude.com/mcp`

Access Jira & Confluence from Claude Command

`claude mcp add --transport http atlassian https://mcp.atlassian.com/v1/mcp`

Access and analyze blockchain data Command

`claude mcp add blockscout --transport http https://mcp.blockscout.com/mcp`

Build applications with compute, storage, and AI Command

`claude mcp add --transport http cloudflare https://bindings.mcp.cloudflare.com/mcp`

Securely access and analyze Egnyte content Command

`claude mcp add --transport http egnyte https://mcp-server.egnyte.com/mcp`

Generate diagrams and better code from Figma context Command

`claude mcp add --transport http figma-remote-mcp https://mcp.figma.com/mcp`

Search and interact with your company knowledge Command

`claude mcp add guru --transport http https://mcp.api.getguru.com/mcp`

Create forms & analyze submissions inside Claude Command

`claude mcp add --transport http jotform https://mcp.jotform.com/mcp-app`

Manage projects, boards, and workflows in monday.com Command

`claude mcp add --transport http monday https://mcp.monday.com/mcp`

Connect your Notion workspace to search, update, and power workflows across tools Command

`claude mcp add --transport http notion https://mcp.notion.com/mcp`

Access PayPal payments platform Command

`claude mcp add --transport http paypal https://mcp.paypal.com/mcp`

Payment processing and financial infrastructure tools Command

```
claude mcp add --transport http stripe https://mcp.stripe.com
```

Manage databases, authentication, and storage Command

```
claude mcp add --transport http supabase https://mcp.supabase.com/mcp
```

Analyze, debug, and manage projects and deployments Command

```
claude mcp add --transport http vercel https://mcp.vercel.com
```

Manage and build sites and apps on Wix Command

`claude mcp add wix --transport http https://mcp.wix.com/mcp`

Access business data from hundreds of sources Command

`claude mcp add --transport http coupler https://mcp.coupler.io/mcp`

Find active tech jobs on Dice Command

`claude mcp add dice --transport http https://mcp.dice.com/mcp`

Read and write Airtable databases

Access and create new content on Miro boards Command

```
claude mcp add --transport http miro https://mcp.miro.com/
```

Search your context lake and safely run actions Requires user-specific URL. [Get your URL here](https://docs.port.io/ai-interfaces/port-mcp-server/overview-and-installation/?mcp-setup=claude&region=eu#installing-port-mcp).

Estimate your federal & state taxes with Aiwyn's tax engine Command

```
claude mcp add --transport http aiwyn-tax https://mcp.columnapi.com/mcp
```

Search and access context from meetings Command

`claude mcp add circleback --transport http https://app.circleback.ai/api/mcp`

Query your CRM. Create records. Ask anything.Command

```
claude mcp add --transport http clarify https://api.clarify.ai/mcp
```

Simulate fund classifications under proposed SFDR 2.0 Command

```
claude mcp add --transport http clarity-ai https://clarity-sfdr20-mcp.pro.clarity.ai/mcp
```

Know everything about your prospects & customers with CRMx Command

`claude mcp add day-ai --transport http https://day.ai/api/mcp`

Access bioRxiv and medRxiv preprint data Command

`claude mcp add biorxiv --transport http https://hcls.mcp.claude.com/biorxiv/mcp`

Access the ChEMBL Database Command

`claude mcp add chembl --transport http https://hcls.mcp.claude.com/chembl/mcp`

Access ClinicalTrials.gov data Command

`claude mcp add clinical-trials --transport http https://hcls.mcp.claude.com/clinical_trials/mcp`

Access the CMS Coverage Database Command

`claude mcp add cms-coverage --transport http https://hcls.mcp.claude.com/cms_coverage/mcp`

Access ICD-10-CM and ICD-10-PCS code sets Command

`claude mcp add icd-10-codes --transport http https://hcls.mcp.claude.com/icd10_codes/mcp`

Access US National Provider Identifier (NPI) Registry Command

`claude mcp add npi-registry --transport http https://hcls.mcp.claude.com/npi_registry/mcp`

Search and update your company's knowledge graph Command

`claude mcp add devrev --transport http https://api.devrev.ai/mcp/v1`

Web Search + Code Docs Search Command

```
claude mcp add --transport http exa https://mcp.exa.ai/mcp
```

Clean Public Equity Fundamental Data Command

```
claude mcp add --transport sse fiscal-ai https://api.fiscal.ai/mcp/sse
```

The AI notepad for meetings Command

```
claude mcp add --transport http granola https://mcp.granola.ai/mcp
```

Discover, research, and enrich companies and people Command

`claude mcp add harmonic --transport http https://mcp.api.harmonic.ai`

Add your meetings context via transcripts and notes Command

```
claude mcp add --transport http krisp https://mcp.krisp.ai/mcp
```

A universal concierge for complex businesses Command

```
claude mcp add --transport http lorikeet https://api.lorikeetcx.ai/v1/mcp
```

Add real-time social media data to your searches Command

`claude mcp add lunarcrush --transport http https://lunarcrush.ai/mcp`

The AI notebook for everything on your mind Command

```
claude mcp add --transport http mem https://mcp.mem.ai/mcp
```

The AI platform for recruiting.Command

```
claude mcp add --transport http metaview https://mcp.metaview.ai/mcp
```

Conduct legal research and create work product Command

```
claude mcp add --transport http midpage https://app.midpage.ai/mcp
```

Enhance responses with scholarly research and citations Command

`claude mcp add scholar-gateway --transport http https://connector.scholargateway.ai/mcp`

From query to qualified lead in seconds.Command

```
claude mcp add --transport http sprouts https://sprouts-mcp-server.kartikay-dhar.workers.dev
```

Power AI Workflows with Customer Context Command

```
claude mcp add --transport http gainsight-staircase-ai https://mcp.staircase.ai/mcp
```

Ask AI about your sales calls, deals & pipeline Command

`claude mcp add sybill --transport http https://mcp.sybill.ai/mcp`

Find company & contact data Command

`claude mcp add vibe-prospecting --transport http https://vibeprospecting.explorium.ai/mcp`

Connect 325+ marketing, analytics and CRM data sources Command

`claude mcp add windsor-ai --transport http https://mcp.windsor.ai`

Create presentations, docs, socials, and sites with AI Command

`claude mcp add gamma --transport http https://mcp.gamma.app/mcp`

Ideate, diagram, and align teams Command

```
claude mcp add --transport http lucid https://mcp.lucid.app/mcp
```

Create, deploy, manage, and secure websites on Netlify.Command

`claude mcp add --transport http netlify https://netlify-mcp.netlify.app/mcp`

Discover, evaluate, and buy solutions for the cloud Command

`claude mcp add aws-marketplace --transport http https://marketplace-mcp.us-east-1.api.aws/mcp`

Find funders who support causes like yours Command

```
claude mcp add --transport http kindora-funder-discovery https://kindora-mcp.azurewebsites.net/mcp/
```

Query your data using natural language through Omni's semantic model Command

```
claude mcp add --transport http omni-analytics https://callbacks.omniapp.co/callback/mcp
```

Autonomous marketing to transform how you work Requires user-specific URL. [Get your URL here](https://developers.activecampaign.com/page/mcp).

SEO & AI search analytics Command

`claude mcp add ahrefs --transport http https://api.ahrefs.com/mcp/mcp`

Craft content that wins AI search Command

`claude mcp add airops --transport http https://app.airops.com/mcp`

Integrate with the Airwallex Platform using Claude Command

```
claude mcp add --transport http airwallex-developer https://mcp-demo.airwallex.com/developer
```

Connect to Asana to coordinate tasks, projects, and goals Command

`claude mcp add --transport http asana https://mcp.asana.com/v2/mcp`

Search, manage, and update your Attio CRM from Claude Command

```
claude mcp add --transport http attio https://mcp.attio.com/mcp
```

Company intelligence & workforce analytics Command

`claude mcp add --transport http auraintelligence https://mcp.auraintelligence.com/mcp`

Connect to R&D data, source experiments, and notebooks Requires user-specific URL. [Get your URL here](https://help.benchling.com/hc/en-us/articles/40342713479437-Benchling-MCP).

Search for and use scientific templates and icons Command

`claude mcp add biorender --transport http https://mcp.services.biorender.com/mcp`

Shorten links, generate QR Codes, and track performance Command

`claude mcp add bitly --transport http https://api-ssl.bitly.com/v4/mcp`

Trusted real-time global financial news provider Command

`claude mcp add --transport http mtnewswire`

Search, access and get insights on your Box content Command

`claude mcp add box --transport http https://mcp.box.com`

Search, create, autofill, and export Canva designs Command

`claude mcp add --transport http canva https://mcp.canva.com/mcp`

Predictive intelligence on private companies Command

```
claude mcp add --transport http cb-insights https://mcp.cbinsights.com
```

Managed MCP platform for 350 sources Command

`claude mcp add cdata-connect-ai --transport http https://mcp.cloud.cdata.com/mcp`

Access your company's SharePoint, OneDrive, Outlook, and Teams directly in Claude Command

`claude mcp add microsoft-365 --transport http https://microsoft365.mcp.claude.com/mcp`

Search biomedical literature from PubMed Command

`claude mcp add pubmed --transport http https://pubmed.mcp.claude.com/mcp`

Find prospects. Research accounts. Personalize outreach Command

```
claude mcp add --transport http clay https://api.clay.com/v3/mcp
```

Add authentication, organizations, and billing Command

```
claude mcp add --transport http clerk https://mcp.clerk.com/mcp
```

Project management & collaboration for teams & agents Command

`claude mcp add clickup --transport http https://mcp.clickup.com/mcp`

Manage, transform and deliver your images & videos Command

`claude mcp add --transport http cloudinary https://asset-management.mcp.cloudinary.com/sse`

Explore scientific research Command

```
claude mcp add --transport http consensus https://mcp.consensus.app/mcp
```

Up-to-date docs for LLMs and AI code editors Command

```
claude mcp add --transport http context7 https://mcp.context7.com/mcp
```

Explore partner data and ecosystem insights in Claude Command

`claude mcp add crossbeam --transport http https://mcp.crossbeam.com`

Real time prices, orders, charts, and more for crypto Command

`claude mcp add --transport http crypto.com https://mcp.crypto.com/market-data/mcp`

Managed MCP servers with Unity Catalog and Mosaic AI Requires user-specific URL. [Get your URL here](https://docs.databricks.com/aws/en/generative-ai/mcp/connect-external-services).

Secure, production-ready AI orchestration for privacy Requires user-specific URL. [Get your URL here](https://docs.datagrail.io/docs/vera/vera-mcp/introduction-and-use).

Get answers from unified feedback of your customers.Command

```
claude mcp add --transport http enterpret-wisdom https://wisdom-api.enterpret.com/server/mcp
```

Discover live entertainment events worldwide Command

```
claude mcp add --transport http fever-event-discovery https://data-search.apigw.feverup.com/mcp
```

Bring enterprise context to Claude and your AI tools Requires user-specific URL. [Get your URL here](https://docs.glean.com/administration/platform/mcp/about).

Build GoCardless payment API integrations Command

```
claude mcp add --transport http gocardless https://mcp.gocardless.com
```

Search domains and check availability Command

`claude mcp add --transport http godaddy https://api.godaddy.com/v1/domains/mcp`

BigQuery: Advanced analytical insights for agents Command

```
claude mcp add --transport http bigquery https://bigquery.googleapis.com/mcp
```

Discover every grant opportunity in existence.Command

```
claude mcp add --transport http granted https://grantedai.com/api/mcp/mcp
```

Connect, control, and automate 1,000+ apps with IFTTT Command

```
claude mcp add --transport http ifttt https://ifttt.com/mcp
```

Clinical trial software and site ranking tools Command

`claude mcp add medidata --transport http https://mcp.imedidata.com/mcp`

Access to Intercom data for better customer insights Command

`claude mcp add --transport http intercom https://mcp.intercom.com/mcp`

Connect and use PlayMCP servers in your toolbox Command

`claude mcp add playmcp --transport http https://playmcp.kakao.com/mcp`

Report, strategize & create with real-time Klaviyo data Command

`claude mcp add klaviyo --transport http https://mcp.klaviyo.com/mcp?include-mcp-app=true`

Search, compare and book flights, dynamic packages (flight + hotel) and hotels across global airlines and hotel suppliers.Command

`claude mcp add lastminute-com --transport http https://mcp.lastminute.com/mcp`

High-quality translation with human verification Command

```
claude mcp add --transport http lilt https://mcp.lilt.com/mcp
```

AI visibility and local search intelligence platform Command

```
claude mcp add --transport sse local-falcon https://mcp.localfalcon.com
```

Manage documents, send signature requests, and convert Markdown to PDF Command

```
claude mcp add --transport http lumin https://mcp.luminpdf.com/mcp
```

Discuss and iterate on Magic Patterns designs Command

```
claude mcp add --transport http magic-patterns https://mcp.magicpatterns.com/mcp
```

Turn Claude into your email marketing assistant Command

```
claude mcp add --transport http mailerlite https://mcp.mailerlite.com/mcp
```

Run Make scenarios and manage your Make account Command

```
claude mcp add --transport http make https://mcp.make.com
```

Browse music charts & your personalized music picks Command

`claude mcp add melon --transport http https://mcp.melon.com/mcp/`

Search, analyze and understand your finances on Mercury Command

`claude mcp add mercury --transport http https://mcp.mercury.com/mcp`

Search trusted Microsoft docs to power your development Command

```
claude mcp add --transport http microsoft-learn https://learn.microsoft.com/api/mcp
```

Analyze, query, and manage your Mixpanel data Command

```
claude mcp add --transport http mixpanel https://mcp.mixpanel.com/mcp
```

Get answers from your data Command

`claude mcp add motherduck --transport http https://api.motherduck.com/mcp`

Connect Claude to NetSuite data for analysis & insights Requires user-specific URL. [Get your URL here](https://system.netsuite.com/mcp/mcpinfo.nl).

Interact with AI agents built for biology Command

`claude mcp add owkin --transport http https://mcp.k.owkin.com/mcp`

Give API context to your coding agents Command

```
claude mcp add --transport http postman https://mcp.postman.com/minimal
```

Financial data and AI infrastructure for company research.Command

```
claude mcp add --transport http quartr https://mcp.quartr.com/mcp
```

Search, access, and analyze your Ramp financial data Command

`claude mcp add --transport http ramp https://ramp-mcp-remote.ramp.com/mcp`

Real time web, mobile app, and market data.Command

```
claude mcp add --transport http similarweb https://mcp.similarweb.com
```

Send messages, create canvases, and fetch Slack data Command

```
claude mcp add --transport http --client-id 1601185624273.8899143856786 --callback-port 3118 slack https://mcp.slack.com/mcp
```

Analyze and manage Smartsheet data with Claude Requires user-specific URL. [Get your URL here](https://help.smartsheet.com/articles/2483656-install-smartsheet-connector-claude#toc-get-started).

Retrieve both structured and unstructured data Requires user-specific URL. [Get your URL here](https://docs.snowflake.com/en/user-guide/admin-account-identifier#label-account-name-find).

Pharmaceutical drug & clinical trial intelligence Command

```
claude mcp add --transport http adisinsight https://adisinsight-mcp.springer.com/mcp
```

Search and manage transaction, merchant, and payment data Command

```
claude mcp add --transport sse square https://mcp.squareup.com/sse
```

Connect your AI agents to the web Command

```
claude mcp add --transport http tavily https://mcp.tavily.com/mcp
```

Search pg and Tiger docs, learn database skills Command

```
claude mcp add --transport http pg-aiguide https://mcp.tigerdata.com/docs
```

Find your ideal hotel at the best price.Command

`claude mcp add --transport http trivago https://mcp.trivago.com/mcp`

Search and explore skill-building resources Command

`claude mcp add udemy-business --transport http https://api.udemy.com/mcp`

Search and manage Pylon support issues Command

```
claude mcp add --transport http pylon https://mcp.usepylon.com/
```

Find people, productivity and business impact insights Requires user-specific URL. [Get your URL here](https://docs.visier.com/developer/agents/mcp/mcp-server-set-up.htm).

Manage Webflow CMS, pages, assets and sites Command

```
claude mcp add --transport http webflow https://mcp.webflow.com/mcp
```

Secure AI access to manage your WordPress.com sites Command

`claude mcp add wordpress-com --transport http https://public-api.wordpress.com/wpcom/v2/mcp/v1`

Automate workflows and connect your business apps Requires user-specific URL. [Get your URL here](https://app.workato.com/ai_hub/mcp).

Discover the right Wyndham Hotel for you, faster Command

```
claude mcp add --transport http wyndham-hotels https://mcp.wyndhamhotels.com/claude/mcp
```

Automate workflows across thousands of apps via conversation Command

`claude mcp add zapier --transport http https://mcp.zapier.com/api/v1/connect`

Zoho Books MCP for Smart Finance Ops Command

```
claude mcp add --transport http zoho-books {url}
```

MCP Server for Zoho CRM Workflows Command

```
claude mcp add --transport http zoho-crm {url}
```

Zoho Desk MCP for Customer Support Automation Command

```
claude mcp add --transport http zoho-desk {url}
```

Zoho Projects MCP for Task & Project Automation Command

```
claude mcp add --transport http zoho-projects {url}
```

Enrich contacts & accounts with GTM intelligence Command

`claude mcp add --transport http zoominfo https://mcp.zoominfo.com/mcp`

Record screen and collect automatic context for issues Command

```
claude mcp add --transport http jam https://mcp.jam.dev/mcp
```

Authenticated access to your Postgres and MySQL DB's Command

```
claude mcp add --transport http planetscale https://mcp.pscale.dev/mcp/planetscale
```

Search, query, and debug errors intelligently Command

`claude mcp add --transport http sentry https://mcp.sentry.dev/mcp`

Notes & second brain Command

```
claude mcp add --transport http craft https://mcp.craft.do/my/mcp
```

India's official statistics via natural language Command

```
claude mcp add --transport http mospi https://mcp.mospi.gov.in/
```

Search Apollo docs, specs, and best practices Command

```
claude mcp add --transport http graphos-tools https://mcp.apollographql.com
```

Explore customer data and generate insights via Claude Requires user-specific URL. [Get your URL here](https://docs.customer.io/ai/mcp-server/).

Query, analyze, and manage your PostHog insights Command

```
claude mcp add --transport http posthog https://mcp.posthog.com/mcp
```

Query and explore observability data and SLOs Command

`claude mcp add --transport http honeycomb https://mcp.honeycomb.io/mcp`

See and manage everything in incident.io Command

`claude mcp add incident-io --transport http https://mcp.incident.io/mcp`

Unleash your team's best performance with Outreach AI Command

```
claude mcp add --transport http outreach https://api.outreach.io/mcp/
```

Connect to Pendo for product and user insights Requires user-specific URL. [Get your URL here](https://support.pendo.io/hc/en-us/articles/41102236924955).

Create, query, and manage structured content in Sanity Command

```
claude mcp add --transport http sanity https://mcp.sanity.io
```

Securely retrieve data from your federated data sources Requires user-specific URL. [Get your URL here](https://docs.starburst.io/starburst-galaxy/ai-workflows/mcp-server.html).

Manage and automate your support tickets Command

```
claude mcp add --transport http unthread https://app.unthread.io/api/mcp
```

Analyze client conversations, patterns, and insights.Command

```
claude mcp add --transport http zocks https://mcp.zocks.io/v1/mcp
```

Research nonprofits and funders using Candid's data Command

`claude mcp add candid --transport http https://mcp.candid.org/mcp`

Drug target discovery and prioritisation platform Command

`claude mcp add open-targets --transport http https://mcp.platform.opentargets.org/mcp`

Search and metadata tools for Synapse scientific data Command

`claude mcp add synapse-org --transport http https://mcp.synapse.org/mcp`

Interact with your Chronograph data directly in Claude Command

`claude mcp add --transport http chronograph https://ai.chronograph.pe/mcp`

## Installing MCP servers

MCP servers can be configured in three different ways depending on your needs:

### Option 1: Add a remote HTTP server

HTTP servers are the recommended option for connecting to remote MCP servers. This is the most widely supported transport for cloud-based services.

```
# Basic syntax
claude mcp add --transport http <name> <url>

# Real example: Connect to Notion
claude mcp add --transport http notion https://mcp.notion.com/mcp

# Example with Bearer token
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

### Option 2: Add a remote SSE server

```
# Basic syntax
claude mcp add --transport sse <name> <url>

# Real example: Connect to Asana
claude mcp add --transport sse asana https://mcp.asana.com/sse

# Example with authentication header
claude mcp add --transport sse private-api https://api.company.com/sse \
  --header "X-API-Key: your-key-here"
```

### Option 3: Add a local stdio server

Stdio servers run as local processes on your machine. They’re ideal for tools that need direct system access or custom scripts.

```
# Basic syntax
claude mcp add [options] <name> -- <command> [args...]

# Real example: Add Airtable server
claude mcp add --transport stdio --env AIRTABLE_API_KEY=YOUR_KEY airtable \
  -- npx -y airtable-mcp-server
```

### Managing your servers

Once configured, you can manage your MCP servers with these commands:

```
# List all configured servers
claude mcp list

# Get details for a specific server
claude mcp get github

# Remove a server
claude mcp remove github

# (within Claude Code) Check server status
/mcp
```

### Dynamic tool updates

Claude Code supports MCP `list_changed` notifications, allowing MCP servers to dynamically update their available tools, prompts, and resources without requiring you to disconnect and reconnect. When an MCP server sends a `list_changed` notification, Claude Code automatically refreshes the available capabilities from that server.

### Automatic reconnection

If an HTTP or SSE server disconnects mid-session, Claude Code automatically reconnects with exponential backoff: up to five attempts, starting at a one-second delay and doubling each time. The server appears as pending in `/mcp` while reconnection is in progress. After five failed attempts the server is marked as failed and you can retry manually from `/mcp`. Stdio servers are local processes and are not reconnected automatically.The same backoff applies when an HTTP or SSE server fails its initial connection at startup. As of v2.1.121, Claude Code retries the initial connection up to three times on transient errors such as a 5xx response, a connection refused, or a timeout, then marks the server as failed if it still cannot connect. Authentication and not-found errors are not retried because they require a configuration change to resolve.

### Push messages with channels

An MCP server can also push messages directly into your session so Claude can react to external events like CI results, monitoring alerts, or chat messages. To enable this, your server declares the `claude/channel` capability and you opt it in with the `--channels` flag at startup. See [Channels](https://code.claude.com/docs/en/channels) to use an officially supported channel, or [Channels reference](https://code.claude.com/docs/en/channels-reference) to build your own.

### Plugin-provided MCP servers

[Plugins](https://code.claude.com/docs/en/plugins) can bundle MCP servers, automatically providing tools and integrations when the plugin is enabled. Plugin MCP servers work identically to user-configured servers.**How plugin MCP servers work**:

*   Plugins define MCP servers in `.mcp.json` at the plugin root or inline in `plugin.json`
*   When a plugin is enabled, its MCP servers start automatically
*   Plugin MCP tools appear alongside manually configured MCP tools
*   Plugin servers are managed through plugin installation (not `/mcp` commands)

**Example plugin MCP configuration**:In `.mcp.json` at plugin root:

```
{
  "mcpServers": {
    "database-tools": {
      "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server",
      "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"],
      "env": {
        "DB_URL": "${DB_URL}"
      }
    }
  }
}
```

Or inline in `plugin.json`:

```
{
  "name": "my-plugin",
  "mcpServers": {
    "plugin-api": {
      "command": "${CLAUDE_PLUGIN_ROOT}/servers/api-server",
      "args": ["--port", "8080"]
    }
  }
}
```

**Plugin MCP features**:

*   **Automatic lifecycle**: At session startup, servers for enabled plugins connect automatically. If you enable or disable a plugin during a session, run `/reload-plugins` to connect or disconnect its MCP servers
*   **Environment variables**: use `${CLAUDE_PLUGIN_ROOT}` for bundled plugin files and `${CLAUDE_PLUGIN_DATA}` for [persistent state](https://code.claude.com/docs/en/plugins-reference#persistent-data-directory) that survives plugin updates
*   **User environment access**: Access to same environment variables as manually configured servers
*   **Multiple transport types**: Support stdio, SSE, and HTTP transports (transport support may vary by server)

**Viewing plugin MCP servers**:

```
# Within Claude Code, see all MCP servers including plugin ones
/mcp
```

Plugin servers appear in the list with indicators showing they come from plugins.**Benefits of plugin MCP servers**:

*   **Bundled distribution**: Tools and servers packaged together
*   **Automatic setup**: No manual MCP configuration needed
*   **Team consistency**: Everyone gets the same tools when plugin is installed

See the [plugin components reference](https://code.claude.com/docs/en/plugins-reference#mcp-servers) for details on bundling MCP servers with plugins.

## MCP installation scopes

MCP servers can be configured at three scopes. The scope you choose controls which projects the server loads in and whether the configuration is shared with your team.

| Scope | Loads in | Shared with team | Stored in |
| --- | --- | --- | --- |
| [Local](https://docs.anthropic.com/en/docs/claude-code/mcp#local-scope) | Current project only | No | `~/.claude.json` |
| [Project](https://docs.anthropic.com/en/docs/claude-code/mcp#project-scope) | Current project only | Yes, via version control | `.mcp.json` in project root |
| [User](https://docs.anthropic.com/en/docs/claude-code/mcp#user-scope) | All your projects | No | `~/.claude.json` |

### Local scope

Local scope is the default. A local-scoped server loads only in the project where you added it and stays private to you. Claude Code stores it in `~/.claude.json` under that project’s path, so the same server won’t appear in your other projects. Use local scope for personal development servers, experimental configurations, or servers with credentials you don’t want in version control.

```
# Add a local-scoped server (default)
claude mcp add --transport http stripe https://mcp.stripe.com

# Explicitly specify local scope
claude mcp add --transport http stripe --scope local https://mcp.stripe.com
```

The command writes the server into the entry for your current project inside `~/.claude.json`. The example below shows the result when you run it from `/path/to/your/project`:

```
{
  "projects": {
    "/path/to/your/project": {
      "mcpServers": {
        "stripe": {
          "type": "http",
          "url": "https://mcp.stripe.com"
        }
      }
    }
  }
}
```

### Project scope

Project-scoped servers enable team collaboration by storing configurations in a `.mcp.json` file at your project’s root directory. This file is designed to be checked into version control, ensuring all team members have access to the same MCP tools and services. When you add a project-scoped server, Claude Code automatically creates or updates this file with the appropriate configuration structure.

```
# Add a project-scoped server
claude mcp add --transport http paypal --scope project https://mcp.paypal.com/mcp
```

The resulting `.mcp.json` file follows a standardized format:

```
{
  "mcpServers": {
    "shared-server": {
      "command": "/path/to/server",
      "args": [],
      "env": {}
    }
  }
}
```

For security reasons, Claude Code prompts for approval before using project-scoped servers from `.mcp.json` files. If you need to reset these approval choices, use the `claude mcp reset-project-choices` command.

### User scope

User-scoped servers are stored in `~/.claude.json` and provide cross-project accessibility, making them available across all projects on your machine while remaining private to your user account. This scope works well for personal utility servers, development tools, or services you frequently use across different projects.

```
# Add a user server
claude mcp add --transport http hubspot --scope user https://mcp.hubspot.com/anthropic
```

### Scope hierarchy and precedence

When the same server is defined in more than one place, Claude Code connects to it once, using the definition from the highest-precedence source:

1.   Local scope
2.   Project scope
3.   User scope
4.   [Plugin-provided servers](https://code.claude.com/docs/en/plugins)
5.   [claude.ai connectors](https://docs.anthropic.com/en/docs/claude-code/mcp#use-mcp-servers-from-claude-ai)

The three scopes match duplicates by name. Plugins and connectors match by endpoint, so one that points at the same URL or command as a server above is treated as a duplicate.

### Environment variable expansion in `.mcp.json`

Claude Code supports environment variable expansion in `.mcp.json` files, allowing teams to share configurations while maintaining flexibility for machine-specific paths and sensitive values like API keys.**Supported syntax:**

*   `${VAR}` - Expands to the value of environment variable `VAR`
*   `${VAR:-default}` - Expands to `VAR` if set, otherwise uses `default`

**Expansion locations:** Environment variables can be expanded in:

*   `command` - The server executable path
*   `args` - Command-line arguments
*   `env` - Environment variables passed to the server
*   `url` - For HTTP server types
*   `headers` - For HTTP server authentication

**Example with variable expansion:**

```
{
  "mcpServers": {
    "api-server": {
      "type": "http",
      "url": "${API_BASE_URL:-https://api.example.com}/mcp",
      "headers": {
        "Authorization": "Bearer ${API_KEY}"
      }
    }
  }
}
```

If a required environment variable is not set and has no default value, Claude Code will fail to parse the config.

## Practical examples

### Example: Monitor errors with Sentry

```
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp
```

Authenticate with your Sentry account:

```
/mcp
```

Then debug production issues:

```
What are the most common errors in the last 24 hours?
```

```
Show me the stack trace for error ID abc123
```

```
Which deployment introduced these new errors?
```

### Example: Connect to GitHub for code reviews

GitHub’s remote MCP server authenticates with a GitHub personal access token passed as a header. To get one, open your [GitHub token settings](https://github.com/settings/personal-access-tokens), generate a new fine-grained token with access to the repositories you want Claude to work with, then add the server:

```
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ \
  --header "Authorization: Bearer YOUR_GITHUB_PAT"
```

Then work with GitHub:

```
Review PR #456 and suggest improvements
```

```
Create a new issue for the bug we just found
```

```
Show me all open PRs assigned to me
```

### Example: Query your PostgreSQL database

```
claude mcp add --transport stdio db -- npx -y @bytebase/dbhub \
  --dsn "postgresql://readonly:pass@prod.db.com:5432/analytics"
```

Then query your database naturally:

```
What's our total revenue this month?
```

```
Show me the schema for the orders table
```

```
Find customers who haven't made a purchase in 90 days
```

## Authenticate with remote MCP servers

Many cloud-based MCP servers require authentication. Claude Code supports OAuth 2.0 for secure connections.

1

2

### Use a fixed OAuth callback port

Some MCP servers require a specific redirect URI registered in advance. By default, Claude Code picks a random available port for the OAuth callback. Use `--callback-port` to fix the port so it matches a pre-registered redirect URI of the form `http://localhost:PORT/callback`.You can use `--callback-port` on its own (with dynamic client registration) or together with `--client-id` (with pre-configured credentials).

```
# Fixed callback port with dynamic client registration
claude mcp add --transport http \
  --callback-port 8080 \
  my-server https://mcp.example.com/mcp
```

### Use pre-configured OAuth credentials

Some MCP servers don’t support automatic OAuth setup via Dynamic Client Registration. If you see an error like “Incompatible auth server: does not support dynamic client registration,” the server requires pre-configured credentials. Claude Code also supports servers that use a Client ID Metadata Document (CIMD) instead of Dynamic Client Registration, and discovers these automatically. If automatic discovery fails, register an OAuth app through the server’s developer portal first, then provide the credentials when adding the server.

1

2

3

### Override OAuth metadata discovery

Point Claude Code at a specific OAuth authorization server metadata URL to bypass the default discovery chain. Set `authServerMetadataUrl` when the MCP server’s standard endpoints error, or when you want to route discovery through an internal proxy. By default, Claude Code first checks RFC 9728 Protected Resource Metadata at `/.well-known/oauth-protected-resource`, then falls back to RFC 8414 authorization server metadata at `/.well-known/oauth-authorization-server`.Set `authServerMetadataUrl` in the `oauth` object of your server’s config in `.mcp.json`:

```
{
  "mcpServers": {
    "my-server": {
      "type": "http",
      "url": "https://mcp.example.com/mcp",
      "oauth": {
        "authServerMetadataUrl": "https://auth.example.com/.well-known/openid-configuration"
      }
    }
  }
}
```

The URL must use `https://`. `authServerMetadataUrl` requires Claude Code v2.1.64 or later. The metadata URL’s `scopes_supported` overrides the scopes the upstream server advertises.

### Restrict OAuth scopes

Set `oauth.scopes` to pin the scopes Claude Code requests during the authorization flow. This is the supported way to restrict an MCP server to a security-team-approved subset when the upstream authorization server advertises more scopes than you want to grant. The value is a single space-separated string, matching the `scope` parameter format in RFC 6749 §3.3.

```
{
  "mcpServers": {
    "slack": {
      "type": "http",
      "url": "https://mcp.slack.com/mcp",
      "oauth": {
        "scopes": "channels:read chat:write search:read"
      }
    }
  }
}
```

`oauth.scopes` takes precedence over both `authServerMetadataUrl` and the scopes the server discovers at `/.well-known`. Leave it unset to let the MCP server determine the requested scope set.If the authorization server advertises `offline_access` in `scopes_supported`, Claude Code appends it to the pinned scopes so the access token can be refreshed without a new browser sign-in.If the server later returns a 403 `insufficient_scope` for a tool call, Claude Code re-authenticates with the same pinned scopes. Widen `oauth.scopes` when a tool you need requires a scope outside the pin.

If your MCP server uses an authentication scheme other than OAuth (such as Kerberos, short-lived tokens, or an internal SSO), use `headersHelper` to generate request headers at connection time. Claude Code runs the command and merges its output into the connection headers.

```
{
  "mcpServers": {
    "internal-api": {
      "type": "http",
      "url": "https://mcp.internal.example.com",
      "headersHelper": "/opt/bin/get-mcp-auth-headers.sh"
    }
  }
}
```

The command can also be inline:

```
{
  "mcpServers": {
    "internal-api": {
      "type": "http",
      "url": "https://mcp.internal.example.com",
      "headersHelper": "echo '{\"Authorization\": \"Bearer '\"$(get-token)\"'\"}'"
    }
  }
}
```

**Requirements:**

*   The command must write a JSON object of string key-value pairs to stdout
*   The command runs in a shell with a 10-second timeout
*   Dynamic headers override any static `headers` with the same name

The helper runs fresh on each connection (at session start and on reconnect). There is no caching, so your script is responsible for any token reuse.Claude Code sets these environment variables when executing the helper:

| Variable | Value |
| --- | --- |
| `CLAUDE_CODE_MCP_SERVER_NAME` | the name of the MCP server |
| `CLAUDE_CODE_MCP_SERVER_URL` | the URL of the MCP server |

Use these to write a single helper script that serves multiple MCP servers.

## Add MCP servers from JSON configuration

If you have a JSON configuration for an MCP server, you can add it directly:

1

2

## Import MCP servers from Claude Desktop

If you’ve already configured MCP servers in Claude Desktop, you can import them:

1

2

3

## Use MCP servers from Claude.ai

If you’ve logged into Claude Code with a [Claude.ai](https://claude.ai/) account, MCP servers you’ve added in Claude.ai are automatically available in Claude Code:

1

2

3

A server you’ve added in Claude Code takes [precedence](https://docs.anthropic.com/en/docs/claude-code/mcp#scope-hierarchy-and-precedence) over a claude.ai connector that points at the same URL. When this happens, `/mcp` lists the connector as hidden and shows how to remove the duplicate if you’d rather use the connector.To disable claude.ai MCP servers in Claude Code, set the `ENABLE_CLAUDEAI_MCP_SERVERS` environment variable to `false`:

```
ENABLE_CLAUDEAI_MCP_SERVERS=false claude
```

## Use Claude Code as an MCP server

You can use Claude Code itself as an MCP server that other applications can connect to:

```
# Start Claude as a stdio MCP server
claude mcp serve
```

You can use this in Claude Desktop by adding this configuration to claude_desktop_config.json:

```
{
  "mcpServers": {
    "claude-code": {
      "type": "stdio",
      "command": "claude",
      "args": ["mcp", "serve"],
      "env": {}
    }
  }
}
```

## MCP output limits and warnings

When MCP tools produce large outputs, Claude Code helps manage the token usage to prevent overwhelming your conversation context:

*   **Output warning threshold**: Claude Code displays a warning when any MCP tool output exceeds 10,000 tokens
*   **Configurable limit**: you can adjust the maximum allowed MCP output tokens using the `MAX_MCP_OUTPUT_TOKENS` environment variable
*   **Default limit**: the default maximum is 25,000 tokens
*   **Scope**: the environment variable applies to tools that don’t declare their own limit. Tools that set [`anthropic/maxResultSizeChars`](https://docs.anthropic.com/en/docs/claude-code/mcp#raise-the-limit-for-a-specific-tool) use that value instead for text content, regardless of what `MAX_MCP_OUTPUT_TOKENS` is set to. Tools that return image data are still subject to `MAX_MCP_OUTPUT_TOKENS`

To increase the limit for tools that produce large outputs:

```
export MAX_MCP_OUTPUT_TOKENS=50000
claude
```

This is particularly useful when working with MCP servers that:

*   Query large datasets or databases
*   Generate detailed reports or documentation
*   Process extensive log files or debugging information

### Raise the limit for a specific tool

If you’re building an MCP server, you can allow individual tools to return results larger than the default persist-to-disk threshold by setting `_meta["anthropic/maxResultSizeChars"]` in the tool’s `tools/list` response entry. Claude Code raises that tool’s threshold to the annotated value, up to a hard ceiling of 500,000 characters.This is useful for tools that return inherently large but necessary outputs, such as database schemas or full file trees. Without the annotation, results that exceed the default threshold are persisted to disk and replaced with a file reference in the conversation.

```
{
  "name": "get_schema",
  "description": "Returns the full database schema",
  "_meta": {
    "anthropic/maxResultSizeChars": 200000
  }
}
```

The annotation applies independently of `MAX_MCP_OUTPUT_TOKENS` for text content, so users don’t need to raise the environment variable for tools that declare it. Tools that return image data are still subject to the token limit.

## Respond to MCP elicitation requests

MCP servers can request structured input from you mid-task using elicitation. When a server needs information it can’t get on its own, Claude Code displays an interactive dialog and passes your response back to the server. No configuration is required on your side: elicitation dialogs appear automatically when a server requests them.Servers can request input in two ways:

*   **Form mode**: Claude Code shows a dialog with form fields defined by the server (for example, a username and password prompt). Fill in the fields and submit.
*   **URL mode**: Claude Code opens a browser URL for authentication or approval. Complete the flow in the browser, then confirm in the CLI.

To auto-respond to elicitation requests without showing a dialog, use the [`Elicitation` hook](https://code.claude.com/docs/en/hooks#elicitation).If you’re building an MCP server that uses elicitation, see the [MCP elicitation specification](https://modelcontextprotocol.io/docs/learn/client-concepts#elicitation) for protocol details and schema examples.

## Use MCP resources

MCP servers can expose resources that you can reference using @ mentions, similar to how you reference files.

### Reference MCP resources

1

2

3

## Scale with MCP Tool Search

Tool search keeps MCP context usage low by deferring tool definitions until Claude needs them. Only tool names load at session start, so adding more MCP servers has minimal impact on your context window.

### How it works

Tool search is enabled by default. MCP tools are deferred rather than loaded into context upfront, and Claude uses a search tool to discover relevant ones when a task needs them. Only the tools Claude actually uses enter context. From your perspective, MCP tools work exactly as before.If you prefer threshold-based loading, set `ENABLE_TOOL_SEARCH=auto` to load schemas upfront when they fit within 10% of the context window and defer only the overflow. See [Configure tool search](https://docs.anthropic.com/en/docs/claude-code/mcp#configure-tool-search) for all options.

If you’re building an MCP server, the server instructions field becomes more useful with Tool Search enabled. Server instructions help Claude understand when to search for your tools, similar to how [skills](https://code.claude.com/docs/en/skills) work.Add clear, descriptive server instructions that explain:

*   What category of tasks your tools handle
*   When Claude should search for your tools
*   Key capabilities your server provides

Claude Code truncates tool descriptions and server instructions at 2KB each. Keep them concise to avoid truncation, and put critical details near the start.

### Configure tool search

Tool search is enabled by default: MCP tools are deferred and discovered on demand. It is disabled by default on Vertex AI, which does not accept the tool search beta header, and when `ANTHROPIC_BASE_URL` points to a non-first-party host, since most proxies do not forward `tool_reference` blocks. Set `ENABLE_TOOL_SEARCH` explicitly to opt in. This feature requires models that support `tool_reference` blocks: Sonnet 4 and later, or Opus 4 and later. Haiku models do not support tool search.Control tool search behavior with the `ENABLE_TOOL_SEARCH` environment variable:

| Value | Behavior |
| --- | --- |
| (unset) | All MCP tools deferred and loaded on demand. Falls back to loading upfront on Vertex AI or when `ANTHROPIC_BASE_URL` is a non-first-party host |
| `true` | All MCP tools deferred, including on Vertex AI and for non-first-party `ANTHROPIC_BASE_URL` |
| `auto` | Threshold mode: tools load upfront if they fit within 10% of the context window, deferred otherwise |
| `auto:<N>` | Threshold mode with a custom percentage, where `<N>` is 0-100 (e.g., `auto:5` for 5%) |
| `false` | All MCP tools loaded upfront, no deferral |

```
# Use a custom 5% threshold
ENABLE_TOOL_SEARCH=auto:5 claude

# Disable tool search entirely
ENABLE_TOOL_SEARCH=false claude
```

Or set the value in your [settings.json `env` field](https://code.claude.com/docs/en/settings#available-settings).You can also disable the `ToolSearch` tool specifically:

```
{
  "permissions": {
    "deny": ["ToolSearch"]
  }
}
```

### Exempt a server from deferral

If a server’s tools should always be visible to Claude without a search step, set `alwaysLoad` to `true` in that server’s configuration. Every tool from that server then loads into context at session start regardless of the `ENABLE_TOOL_SEARCH` setting. Use this for a small number of tools that Claude needs on every turn, since each upfront tool consumes context that would otherwise be available for your conversation.The following `.mcp.json` entry exempts one HTTP server while leaving other servers deferred:

```
{
  "mcpServers": {
    "core-tools": {
      "type": "http",
      "url": "https://mcp.example.com/mcp",
      "alwaysLoad": true
    }
  }
}
```

The `alwaysLoad` field is available on all server types and requires Claude Code v2.1.121 or later. An MCP server can also mark individual tools as always-loaded by including `"anthropic/alwaysLoad": true` in the tool’s `_meta` object, which has the same effect for that tool only.

## Use MCP prompts as commands

MCP servers can expose prompts that become available as commands in Claude Code.

### Execute MCP prompts

1

2

3

## Managed MCP configuration

For organizations that need centralized control over MCP servers, Claude Code supports two configuration options:

1.   **Exclusive control with `managed-mcp.json`**: Deploy a fixed set of MCP servers that users cannot modify or extend
2.   **Policy-based control with allowlists/denylists**: Allow users to add their own servers, but restrict which ones are permitted

These options allow IT administrators to:

*   **Control which MCP servers employees can access**: Deploy a standardized set of approved MCP servers across the organization
*   **Prevent unauthorized MCP servers**: Restrict users from adding unapproved MCP servers
*   **Disable MCP entirely**: Remove MCP functionality completely if needed

### Option 1: Exclusive control with managed-mcp.json

When you deploy a `managed-mcp.json` file, it takes **exclusive control** over all MCP servers. Users cannot add, modify, or use any MCP servers other than those defined in this file. This is the simplest approach for organizations that want complete control.System administrators deploy the configuration file to a system-wide directory:

*   macOS: `/Library/Application Support/ClaudeCode/managed-mcp.json`
*   Linux and WSL: `/etc/claude-code/managed-mcp.json`
*   Windows: `C:\Program Files\ClaudeCode\managed-mcp.json`

The `managed-mcp.json` file uses the same format as a standard `.mcp.json` file:

```
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    },
    "sentry": {
      "type": "http",
      "url": "https://mcp.sentry.dev/mcp"
    },
    "company-internal": {
      "type": "stdio",
      "command": "/usr/local/bin/company-mcp-server",
      "args": ["--config", "/etc/company/mcp-config.json"],
      "env": {
        "COMPANY_API_URL": "https://internal.company.com"
      }
    }
  }
}
```

### Option 2: Policy-based control with allowlists and denylists

Instead of taking exclusive control, administrators can allow users to configure their own MCP servers while enforcing restrictions on which servers are permitted. This approach uses `allowedMcpServers` and `deniedMcpServers` in the [managed settings file](https://code.claude.com/docs/en/settings#settings-files).

#### Restriction options

Each entry in the allowlist or denylist can restrict servers in three ways:

1.   **By server name** (`serverName`): Matches the configured name of the server
2.   **By command** (`serverCommand`): Matches the exact command and arguments used to start stdio servers
3.   **By URL pattern** (`serverUrl`): Matches remote server URLs with wildcard support

**Important**: Each entry must have exactly one of `serverName`, `serverCommand`, or `serverUrl`.

#### Example configuration

```
{
  "allowedMcpServers": [
    // Allow by server name
    { "serverName": "github" },
    { "serverName": "sentry" },

    // Allow by exact command (for stdio servers)
    { "serverCommand": ["npx", "-y", "@modelcontextprotocol/server-filesystem"] },
    { "serverCommand": ["python", "/usr/local/bin/approved-server.py"] },

    // Allow by URL pattern (for remote servers)
    { "serverUrl": "https://mcp.company.com/*" },
    { "serverUrl": "https://*.internal.corp/*" }
  ],
  "deniedMcpServers": [
    // Block by server name
    { "serverName": "dangerous-server" },

    // Block by exact command (for stdio servers)
    { "serverCommand": ["npx", "-y", "unapproved-package"] },

    // Block by URL pattern (for remote servers)
    { "serverUrl": "https://*.untrusted.com/*" }
  ]
}
```

#### How command-based restrictions work

**Exact matching**:

*   Command arrays must match **exactly** - both the command and all arguments in the correct order
*   Example: `["npx", "-y", "server"]` will NOT match `["npx", "server"]` or `["npx", "-y", "server", "--flag"]`

**Stdio server behavior**:

*   When the allowlist contains **any**`serverCommand` entries, stdio servers **must** match one of those commands
*   Stdio servers cannot pass by name alone when command restrictions are present
*   This ensures administrators can enforce which commands are allowed to run

**Non-stdio server behavior**:

*   Remote servers (HTTP, SSE, WebSocket) use URL-based matching when `serverUrl` entries exist in the allowlist
*   If no URL entries exist, remote servers fall back to name-based matching
*   Command restrictions do not apply to remote servers

#### How URL-based restrictions work

URL patterns support wildcards using `*` to match any sequence of characters. This is useful for allowing entire domains or subdomains.**Wildcard examples**:

*   `https://mcp.company.com/*` - Allow all paths on a specific domain
*   `https://*.example.com/*` - Allow any subdomain of example.com
*   `http://localhost:*/*` - Allow any port on localhost

**Remote server behavior**:

*   When the allowlist contains **any**`serverUrl` entries, remote servers **must** match one of those URL patterns
*   Remote servers cannot pass by name alone when URL restrictions are present
*   This ensures administrators can enforce which remote endpoints are allowed

Example: URL-only allowlist

```
{
  "allowedMcpServers": [
    { "serverUrl": "https://mcp.company.com/*" },
    { "serverUrl": "https://*.internal.corp/*" }
  ]
}
```

**Result**:

*   HTTP server at `https://mcp.company.com/api`: ✅ Allowed (matches URL pattern)
*   HTTP server at `https://api.internal.corp/mcp`: ✅ Allowed (matches wildcard subdomain)
*   HTTP server at `https://external.com/mcp`: ❌ Blocked (doesn’t match any URL pattern)
*   Stdio server with any command: ❌ Blocked (no name or command entries to match)

Example: Command-only allowlist

```
{
  "allowedMcpServers": [
    { "serverCommand": ["npx", "-y", "approved-package"] }
  ]
}
```

**Result**:

*   Stdio server with `["npx", "-y", "approved-package"]`: ✅ Allowed (matches command)
*   Stdio server with `["node", "server.js"]`: ❌ Blocked (doesn’t match command)
*   HTTP server named “my-api”: ❌ Blocked (no name entries to match)

Example: Mixed name and command allowlist

```
{
  "allowedMcpServers": [
    { "serverName": "github" },
    { "serverCommand": ["npx", "-y", "approved-package"] }
  ]
}
```

**Result**:

*   Stdio server named “local-tool” with `["npx", "-y", "approved-package"]`: ✅ Allowed (matches command)
*   Stdio server named “local-tool” with `["node", "server.js"]`: ❌ Blocked (command entries exist but doesn’t match)
*   Stdio server named “github” with `["node", "server.js"]`: ❌ Blocked (stdio servers must match commands when command entries exist)
*   HTTP server named “github”: ✅ Allowed (matches name)
*   HTTP server named “other-api”: ❌ Blocked (name doesn’t match)

Example: Name-only allowlist

```
{
  "allowedMcpServers": [
    { "serverName": "github" },
    { "serverName": "internal-tool" }
  ]
}
```

**Result**:

*   Stdio server named “github” with any command: ✅ Allowed (no command restrictions)
*   Stdio server named “internal-tool” with any command: ✅ Allowed (no command restrictions)
*   HTTP server named “github”: ✅ Allowed (matches name)
*   Any server named “other”: ❌ Blocked (name doesn’t match)

#### Allowlist behavior (`allowedMcpServers`)

*   `undefined` (default): No restrictions - users can configure any MCP server
*   Empty array `[]`: Complete lockdown - users cannot configure any MCP servers
*   List of entries: Users can only configure servers that match by name, command, or URL pattern

#### Denylist behavior (`deniedMcpServers`)

*   `undefined` (default): No servers are blocked
*   Empty array `[]`: No servers are blocked
*   List of entries: Specified servers are explicitly blocked across all scopes

#### Important notes

*   **Option 1 and Option 2 can be combined**: If `managed-mcp.json` exists, it has exclusive control and users cannot add servers. Allowlists/denylists still apply to the managed servers themselves.
*   **Denylist takes absolute precedence**: If a server matches a denylist entry (by name, command, or URL), it will be blocked even if it’s on the allowlist
*   Name-based, command-based, and URL-based restrictions work together: a server passes if it matches **either** a name entry, a command entry, or a URL pattern (unless blocked by denylist)
