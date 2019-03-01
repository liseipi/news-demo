'use strict'

const Schema = use('Schema')

class CommentsReplySchema extends Schema {
  up () {
    this.create('cs_comments_reply', (table) => {
      table.increments('id')
      table.integer('parent').comment('父级评论id')
      table.integer('reply').comment('回复评论id')
      table.boolean('status').defaultTo(0).comment('评论的状态，禁止/显示')
      table.timestamps()
    })
  }

  down () {
    this.drop('cs_comments_reply')
  }
}

module.exports = CommentsReplySchema
