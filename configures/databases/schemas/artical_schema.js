'use strict'

const Schema = use('Schema')

class ArticleSchema extends Schema {
  up () {
    this.create('cs_artical', (table) => {
      table.increments('id')
      table.integer('category_id').unsigned().index().comment('分类栏目ID')
      table.foreign('category_id').references('cs_category.id')
      table.string('title').notNullable().comment('文章标题')
      table.string('vice_title').comment('文章副标题')
      table.string('originlink').comment('源链接')
      table.integer('user_id').unsigned().index().comment('文章作者-管理员')
      table.foreign('user_id').references('ni_admin_user.ni_id')
      table.boolean('status').defaultTo(0).comment('状态：(0=显示，1=下线)')
      table.boolean('comment_status').defaultTo(0).comment('文章评论状态：(0=开启，1=禁止)')
      table.integer('source').comment('文章来源: (1=站内原创，2=改编，3=采集， 4=爬虫)')
      table.string('source_file').comment('爬虫的文件名称')
      table.integer('sort').comment('排序')
      table.string('thumb_img').comment('缩略图片')
      table.string('keywords').comment('关键字')
      table.text('description').comment('概要')
      table.text('content', 'longtext').comment('正文内容')
      table.integer('view_count').defaultTo(0).comment('查看次数')
      table.timestamps()
    })
      .raw("ALTER TABLE `cs_artical` AUTO_INCREMENT=6000")
  }

  down () {
    this.drop('cs_artical')
  }
}

module.exports = ArticleSchema
