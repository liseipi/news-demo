'use strict'

const Schema = use('Schema')

class CategorySchema extends Schema {
  up () {
    this.create('cs_category', (table) => {
      table.increments('id')
      table.string('name').notNullable().comment('栏目名称')
      table.integer('parent').notNullable().comment('父级ID')
      table.string('controller').comment('路由名称')
      table.text('description').comment('描述')
      table.integer('sort').comment('排序')
      table.boolean('status').defaultTo(0).comment('状态: (0=显示), (1=隐藏)')
      table.integer('column_type').comment('类型')
      table.timestamps()
    })
      .raw("ALTER TABLE `cs_category` AUTO_INCREMENT=1000")
  }

  down () {
    this.drop('cs_category')
  }
}

module.exports = CategorySchema
