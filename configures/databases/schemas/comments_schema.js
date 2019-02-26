'use strict'

const Schema = use('Schema')

class CommentsSchema extends Schema {
  up () {
    this.create('cs_comments', (table) => {
      table.increments('id')
      table.integer('article_id').unsigned().index()
      table.foreign('article_id').references('cs_article.id').onDelete('CASCADE')
      table.integer('customer_id').unsigned().index()
      table.foreign('customer_id').references('cs_customers.id').onDelete('CASCADE')
      table.string('contents').comment('评论内容')
      table.boolean('status').defaultTo(0).comment('评论的状态，禁止/显示')
      table.timestamps()
    })
  }

  down () {
    this.drop('cs_comments')
  }
}

module.exports = CommentsSchema
